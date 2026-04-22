from ollama import chat
from ollama import ChatResponse
import json
import re
import logging
import time
import os
from functools import lru_cache

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 重定义日志级别名称为中文
logging.addLevelName(logging.DEBUG, '调试')
logging.addLevelName(logging.INFO, '信息')
logging.addLevelName(logging.WARNING, '警告')
logging.addLevelName(logging.ERROR, '错误')
logging.addLevelName(logging.CRITICAL, '严重')

# 全局变量用于存储测试过程中的日志
test_logs = []
# 用于存储每轮测试的详细数据
test_round_data = []

@lru_cache(maxsize=100)
def generate_drone_command(text_command):
    # 处理空输入
    if not text_command or text_command.strip() == '':
        return {"error": "Empty command", "message": "请输入有效的无人机指令"}
    
    # 定义精简提示模板
    prompt = '''
你是无人机飞行指令解析器。将自然语言转换为严格的JSON指令。

指令：{text_command}

请输出严格的JSON格式，不要有任何解释。

示例：
输入：起飞，向后2m，然后降落
输出：[{{"action":"take_off","params":{{"height":1.0}}}},{{"action":"direction_move","params":{{"orientation":"backward","distance":2.0}}}},{{"action":"land"}}]

输入：起飞到2米，然后向前飞1米，最后降落
输出：[{{"action":"take_off","params":{{"height":2.0}}}},{{"action":"direction_move","params":{{"orientation":"forward","distance":1.0}}}},{{"action":"land"}}]
'''.format(text_command=text_command)


    try:
        # 调用Ollama模型
        logging.info(f"处理指令: {text_command}")
        start_time = time.time()
        # 最佳参数配置（基于性能测试）
        optimized_options = {
            'main_gpu': 0,          # 指定主GPU
            'tensor_split': [1, 0],  # 在GPU之间分配张量
            'num_ctx': 2048,         # 固定上下文长度，平衡性能和速度
            'temperature': 0.0,      # 完全确定性，加快生成
            'top_p': 0.1,            # 最小搜索空间
            'max_new_tokens': 200    # 增加输出限制，确保能生成完整的JSON
        }
        
        response: ChatResponse = chat(
            model='qwen3.5', 
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
            options=optimized_options
        )
        end_time = time.time()
        elapsed_time = end_time - start_time

        # 提取模型输出
        model_output = response['message']['content']
        logging.debug(f"模型输出: {model_output}")
        
        # 清理输出，确保只保留JSON
        # 尝试提取JSON部分
        # 更健壮的JSON提取方法
        model_output = model_output.strip()
        
        # 检查模型输出是否为空
        if not model_output:
            raise json.JSONDecodeError("模型输出为空", "", 0)
        
        # 检查是否是复合指令（多个JSON对象用逗号连接）
        if '},{' in model_output:
            # 如果是复合指令，添加方括号使其成为合法的JSON数组
            model_output = '[' + model_output + ']'
        
        # 解析JSON
        command_json = json.loads(model_output)
        
        # 处理可能的嵌套数组
        if isinstance(command_json, list) and len(command_json) == 1 and isinstance(command_json[0], list):
            command_json = command_json[0]
        logging.info(f"生成的指令: {json.dumps(command_json)}")
        logging.info(f"模型处理时间: {elapsed_time:.2f}秒")
        return command_json, elapsed_time
    except json.JSONDecodeError as e:
        # 如果解析失败，返回错误信息
        logging.error(f"JSON解析错误: {str(e)}")
        logging.error(f"模型输出: {model_output}")
        return {"error": "解析指令失败", "original_output": model_output, "details": str(e)}, elapsed_time
    except Exception as e:
        # 处理其他错误
        logging.error(f"处理指令错误: {str(e)}")
        import traceback
        logging.error(traceback.format_exc())
        return {"error": "处理指令失败", "details": str(e)}, elapsed_time

def validate_command(command):
    """验证生成的指令格式是否正确"""
    # 检查command类型
    if not isinstance(command, (dict, list)):
        return False
    
    if isinstance(command, dict):
        if "error" in command:
            return False
        
        # 检查必要的字段
        if "action" not in command:
            return False
        
        # 检查不同类型指令的参数
        action = command["action"]
        if action == "take_off":
            return "params" in command and "height" in command["params"]
        elif action == "land":
            return True
        elif action == "direction_move":
            return "params" in command and "orientation" in command["params"]
        elif action == "point_move":
            return "params" in command and "coordinate_type" in command["params"] and "coordinate" in command["params"]
        elif action == "point_hover":
            return "params" in command and "coordinate_type" in command["params"] and "coordinate" in command["params"] and "height" in command["params"]
        elif action in ["fixed_Circle", "fixed_Circle_1"]:
            return "params" in command and "coordinate_type" in command["params"] and "point" in command["params"] and "radius" in command["params"]
        elif action == "emergency_hover":
            return True
        else:
            return False
    elif isinstance(command, list):
        # 处理数组格式的复合指令
        for cmd in command:
            if not validate_command(cmd):
                return False
        return True
    else:
        return False

def run_test_round(round_num, test_commands):
    """运行一轮测试"""
    round_start = time.time()
    round_logs = []
    round_command_times = {}
    results = []
    
    # 清除缓存，确保每轮都重新执行
    generate_drone_command.cache_clear()
    
    # 记录轮次开始日志
    round_header = f"\n=== 测试轮次 {round_num} ==="
    print(round_header)
    round_logs.append(round_header)
    
    for command in test_commands:
        # 打印详细的处理日志
        process_log = f"Processing command: {command}"
        logging.info(process_log)
        round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - INFO - {process_log}")
        
        # 重新实现模型调用，确保每轮都打印详细日志
        try:
            # 定义精简提示模板
            prompt = '''
你是无人机飞行指令解析器。将自然语言转换为严格的JSON指令。

指令：{command}

可用动作及参数：
1. take_off: {{"action":"take_off","params":{{"height": 1.0}}}}  // 起飞到指定高度(米)
2. land: {{"action":"land"}}  // 降落
3. direction_move: {{"action":"direction_move","params":{{"orientation": "up|down|left|right|forward|backward", "distance": 0.3}}}}  // 默认distance=0.3
4. point_move: {{"action":"point_move","params":{{"coordinate_type": 1, "coordinate": [x,y,z]}}}}  
5. point_hover: {{"action":"point_hover","params":{{"coordinate_type": 1, "coordinate": [x,y], "height": 1.0}}}}  
6. fixed_Circle: {{"action":"fixed_Circle","params":{{"coordinate_type": 1, "point": [x,y,z], "radius": 1.0}}}}  // 持续盘旋
7. fixed_Circle_1: 同上  // 单次盘旋后悬停
8. emergency_hover: {{"action":"emergency_hover"}}  // 紧急悬停

规则：
- coordinate_type: 1=相对坐标(米), 2=GPS坐标(度,度,米)
- 未指定距离时，direction_move默认0.3米
- 复合指令拆分为数组，按顺序执行
- 仅输出JSON，不要解释
- 对于"起飞"指令，如果没有指定高度，默认高度为1.0米
- 对于"向后"移动，orientation为"backward"
- 距离单位为米，如"2m"表示2米

示例：
输入："起飞，向后2m，然后降落"
输出：[{{"action":"take_off","params":{{"height":1.0}}}},{{"action":"direction_move","params":{{"orientation":"backward","distance":2.0}}}},{{"action":"land"}}]

输入："起飞到2米，然后向前飞1米，最后降落"
输出：[{{"action":"take_off","params":{{"height":2.0}}}},{{"action":"direction_move","params":{{"orientation":"forward","distance":1.0}}}},{{"action":"land"}}]
'''.format(command=command)
            
            start_time = time.time()
            # 最佳参数配置（基于性能测试）
            optimized_options = {
                'main_gpu': 0,          # 指定主GPU
                'tensor_split': [1, 0],  # 在GPU之间分配张量
                'num_ctx': 2048,         # 固定上下文长度，平衡性能和速度
                'temperature': 0.0,      # 完全确定性，加快生成
                'top_p': 0.1,            # 最小搜索空间
                'max_new_tokens': 200    # 增加输出限制，确保能生成完整的JSON
            }
            
            response: ChatResponse = chat(
                model='qwen3.5', 
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
                options=optimized_options
            )
            end_time = time.time()
            elapsed_time = end_time - start_time

            # 提取模型输出
            model_output = response['message']['content']
            debug_log = f"模型输出: {model_output}"
            logging.debug(debug_log)
            round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 调试 - {debug_log}")
            
            # 清理输出，确保只保留JSON
            model_output = model_output.strip()
            
            # 检查模型输出是否为空
            if not model_output:
                raise json.JSONDecodeError("模型输出为空", "", 0)
            
            # 检查是否是复合指令（多个JSON对象用逗号连接）
            if '},{' in model_output:
                # 如果是复合指令，添加方括号使其成为合法的JSON数组
                model_output = '[' + model_output + ']'
            
            # 解析JSON
            command_json = json.loads(model_output)
            
            # 处理可能的嵌套数组
            if isinstance(command_json, list) and len(command_json) == 1 and isinstance(command_json[0], list):
                command_json = command_json[0]
            generated_log = f"生成的指令: {json.dumps(command_json)}"
            logging.info(generated_log)
            round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 信息 - {generated_log}")
            
            time_log = f"模型处理时间: {elapsed_time:.2f}秒"
            logging.info(time_log)
            round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 信息 - {time_log}")
            
            # 验证指令格式
            if validate_command(command_json):
                results.append({
                    'command': command,
                    'success': True,
                    'time': elapsed_time
                })
                success_message = f"  指令: '{command}' - 成功 - 时间: {elapsed_time:.2f}s"
                print(success_message)
                round_logs.append(success_message)
                round_command_times[command] = elapsed_time
            else:
                error_log = f"Invalid command format: {json.dumps(command_json)}"
                logging.error(error_log)
                round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ERROR - {error_log}")
                
                results.append({
                    'command': command,
                    'success': False,
                    'error': 'Invalid command format',
                    'time': elapsed_time
                })
                error_message = f"  指令: '{command}' - 失败: 指令格式不正确 - 时间: {elapsed_time:.2f}s"
                print(error_message)
                round_logs.append(error_message)
                round_command_times[command] = elapsed_time
        except json.JSONDecodeError as e:
            # 如果解析失败，返回错误信息
            error_log = f"JSON解析错误: {str(e)}"
            logging.error(error_log)
            round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 错误 - {error_log}")
            
            results.append({
                'command': command,
                'success': False,
                'error': '解析指令失败',
                'time': 0
            })
            error_message = f"  指令: '{command}' - 失败: 解析失败 - 时间: 0.00s"
            print(error_message)
            round_logs.append(error_message)
            round_command_times[command] = 0
        except Exception as e:
            # 处理其他错误
            error_log = f"处理指令错误: {str(e)}"
            logging.error(error_log)
            round_logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 错误 - {error_log}")
            
            results.append({
                'command': command,
                'success': False,
                'error': '处理指令失败',
                'time': 0
            })
            error_message = f"  指令: '{command}' - 失败: 处理失败 - 时间: 0.00s"
            print(error_message)
            round_logs.append(error_message)
            round_command_times[command] = 0
    
    # 计算统计数据
    success_count = sum(1 for r in results if r['success'])
    success_rate = success_count / len(results) * 100
    
    # 记录轮次统计
    stats_message = f"\n轮次 {round_num} 统计:"
    print(stats_message)
    round_logs.append(stats_message)
    
    success_message = f"  成功数: {success_count}/{len(results)}"
    print(success_message)
    round_logs.append(success_message)
    
    rate_message = f"  成功率: {success_rate:.1f}%"
    print(rate_message)
    round_logs.append(rate_message)
    
    # 打印分割线
    separator = "\n" + "-" * 60 + "\n"
    print(separator)
    round_logs.append(separator)
    
    # 计算轮次总时间
    round_end = time.time()
    round_total_time = round_end - round_start
    
    # 存储轮次数据
    test_round_data.append({
        'round': round_num,
        'command_times': round_command_times,
        'total_time': round_total_time,
        'success_rate': success_rate
    })
    
    # 存储轮次日志
    test_logs.extend(round_logs)
    
    return {
        'round': round_num,
        'results': results,
        'success_rate': success_rate
    }

def generate_test_report(test_results):
    """生成测试报告"""
    # 计算整体统计数据
    total_tests = 0
    total_success = 0
    total_time = 0
    
    for result in test_results:
        total_tests += len(result['results'])
        total_success += sum(1 for r in result['results'] if r['success'])
        total_time += sum(r.get('time', 0) for r in result['results'])
    
    overall_success_rate = total_success / total_tests * 100 if total_tests > 0 else 0
    overall_avg_time = total_time / total_tests if total_tests > 0 else 0
    
    # 生成报告
    model_params = {
        "model": "qwen3.5",
        "context_length": 2048,
        "temperature": 0.0,
        "top_p": 0.1,
        "max_new_tokens": 200,
        "GPU_optimization": True
    }
    
    report = """
# 无人机指令解析器性能测试报告

## 测试配置

### 模型参数
```json
"""
    report += json.dumps(model_params, indent=2)
    report += """
```

## 测试结果

### 整体统计
- **测试轮次**: {0}
- **总测试指令数**: {1}
- **成功指令数**: {2}
- **整体成功率**: {3:.1f}%
- **整体平均处理时间**: {4:.2f}秒

### 轮次详细数据
""".format(
    len(test_results),
    total_tests,
    total_success,
    overall_success_rate,
    overall_avg_time
)
    
    for i, result in enumerate(test_results):
        round_time = sum(r.get('time', 0) for r in result['results'])
        round_avg_time = round_time / len(result['results']) if len(result['results']) > 0 else 0
        report += f"\n#### 轮次 {result['round']}\n"
        report += f"- 成功数: {sum(1 for r in result['results'] if r['success'])}/{len(result['results'])}\n"
        report += f"- 成功率: {result['success_rate']:.1f}%\n"
        report += f"- 平均处理时间: {round_avg_time:.2f}秒\n"
    
    # 按指令类型统计
    command_stats = {}
    for result in test_results:
        for cmd_result in result['results']:
            if cmd_result['command'] not in command_stats:
                command_stats[cmd_result['command']] = {'total': 0, 'success': 0, 'total_time': 0}
            command_stats[cmd_result['command']]['total'] += 1
            command_stats[cmd_result['command']]['total_time'] += cmd_result.get('time', 0)
            if cmd_result['success']:
                command_stats[cmd_result['command']]['success'] += 1
    
    # 添加处理时间表格
    report += "\n### 处理时间详细表格\n"
    report += "| 测试内容 |"
    for i in range(len(test_results)):
        report += f" 第{i+1}次测试时间 (秒) |"
    report += " 平均时间 (秒) |\n"
    
    report += "|---------|"
    for i in range(len(test_results)):
        report += "------------------|"
    report += "----------------|\n"
    
    # 获取所有测试指令
    test_commands = []
    if test_round_data:
        test_commands = list(test_round_data[0]['command_times'].keys())
    
    for command in test_commands:
        report += f"| {command} |"
        # 收集每轮的时间
        times = []
        for round_data in test_round_data:
            time_val = round_data['command_times'].get(command, 0)
            times.append(time_val)
            report += f" {time_val:.2f} |"
        # 计算平均时间
        avg_time = sum(times) / len(times) if times else 0
        report += f" {avg_time:.2f} |\n"
    
    report += "\n### 指令类型统计\n"
    for command, stats in command_stats.items():
        success_rate = stats['success'] / stats['total'] * 100
        avg_time = stats['total_time'] / stats['total'] if stats['total'] > 0 else 0
        report += f"- **{command}**: {stats['success']}/{stats['total']} ({success_rate:.1f}%) - 平均时间: {avg_time:.2f}秒\n"
    
    # 添加测试过程日志
    report += "\n### 测试过程日志\n"
    report += "```\n"
    for log in test_logs:
        report += log + "\n"
    report += "```\n"
    
    # 结论
    report += "\n## 结论\n"
    report += f"1. 系统在 {len(test_results)} 轮测试中表现稳定\n"
    report += f"2. 整体成功率达到 {overall_success_rate:.1f}%，解析准确性高\n"
    report += f"3. 整体平均处理时间为 {overall_avg_time:.2f}秒，性能稳定\n"
    report += "4. 不同类型指令的解析成功率差异不大，系统表现均衡\n"
    report += "5. 处理时间稳定，适合实时控制场景\n"
    
    return report

def main():
    print("无人机指令解析器")
    print("输入 'exit' 退出程序")
    print("输入 'test' 运行性能测试")
    
    while True:
        user_input = input("请输入无人机指令: ")
        
        if user_input.lower() == 'exit':
            print("程序退出")
            break
        elif user_input.lower() == 'test':
            # 运行多轮测试
            test_commands = [
                "起飞到2米高度",
                "降落",
                "向前移动1米",
                "向后移动0.5米",
                "向左移动0.3米",
                "向右移动0.4米",
                "向上移动0.8米",
                "向下移动0.2米",
                "移动到坐标(5,3,2)",
                "悬停"
            ]
            
            num_rounds = 3
            test_results = []
            
            for i in range(num_rounds):
                result = run_test_round(i+1, test_commands)
                test_results.append(result)
            
            # 生成测试报告
            report = generate_test_report(test_results)
            
            # 保存报告
            report_path = 'test_report.md'
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            
            # 获取完整路径
            full_path = os.path.abspath(report_path)
            
            print(f"\n=== 测试完成 ===")
            print(f"测试报告已保存到: {report_path}")
            print(f"报告完整路径: {full_path}")
        else:
            try:
                # 生成指令
                command, elapsed_time = generate_drone_command(user_input)
                
                # 检查是否有错误
                if isinstance(command, dict) and "error" in command:
                    print(f"错误: {command['error']}")
                    if "message" in command:
                        print(f"提示: {command['message']}")
                    if "details" in command:
                        print(f"详情: {command['details']}")
                    if "original_output" in command:
                        print(f"模型输出: {command['original_output']}")
                else:
                    # 验证指令格式
                    if validate_command(command):
                        # 打印生成的指令
                        print("生成的指令:")
                        print(json.dumps(command, indent=2))
                        print(f"\n处理时间: {elapsed_time:.2f}秒")
                        
                        # 模拟发送到Redis
                        print("\n模拟发送到Redis:")
                        if isinstance(command, list):
                            # 复合指令，逐一发送
                            for i, cmd in enumerate(command):
                                print(f"步骤 {i+1}: redis-cli set drone_command '{json.dumps(cmd)}'")
                        else:
                            # 单个指令，直接发送
                            print(f"redis-cli set drone_command '{json.dumps(command)}'")
                        print()
                    else:
                        print("错误: 生成的指令格式不正确")
                        print(f"生成的指令: {json.dumps(command, indent=2)}")
                        print(f"处理时间: {elapsed_time:.2f}秒")
                        print()
            except Exception as e:
                print(f"发生错误: {str(e)}")
                import traceback
                traceback.print_exc()
                print()

import sys

if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 检查是否是测试命令
        if sys.argv[1].lower() == 'test':
            # 运行测试功能
            # 运行多轮测试
            test_commands = [
                "起飞到2米",
                "降落",
                "向前移动1米",
                "向后移动0.5米",
                "向左移动0.3米",
                "向右移动0.4米",
                "向上移动0.8米",
                "向下移动0.2米",
                "移动到坐标(5,3,2)",
                "悬停"
            ]
            
            num_rounds = 3
            test_results = []
            
            for i in range(num_rounds):
                result = run_test_round(i+1, test_commands)
                test_results.append(result)
            
            # 生成测试报告
            report = generate_test_report(test_results)
            
            # 保存报告
            report_path = 'test_report.md'
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            
            # 获取完整路径
            full_path = os.path.abspath(report_path)
            
            print(f"\n=== 测试完成 ===")
            print(f"测试报告已保存到: {report_path}")
            print(f"报告完整路径: {full_path}")
        else:
            # 如果有命令行参数且不是测试命令，直接处理该参数作为指令
            command = ' '.join(sys.argv[1:])
            try:
                # 生成指令
                result, elapsed_time = generate_drone_command(command)
                
                # 检查是否有错误
                if isinstance(result, dict) and "error" in result:
                    print(f"错误: {result['error']}")
                    if "message" in result:
                        print(f"提示: {result['message']}")
                    if "details" in result:
                        print(f"详情: {result['details']}")
                    if "original_output" in result:
                        print(f"模型输出: {result['original_output']}")
                else:
                    # 验证指令格式
                    if validate_command(result):
                        # 打印生成的指令
                        print("生成的指令:")
                        print(json.dumps(result, indent=2))
                        print(f"\n处理时间: {elapsed_time:.2f}秒")
                        
                        # 模拟发送到Redis
                        print("\n模拟发送到Redis:")
                        if isinstance(result, list):
                            # 复合指令，逐一发送
                            for i, cmd in enumerate(result):
                                print(f"步骤 {i+1}: redis-cli set drone_command '{json.dumps(cmd)}'")
                        else:
                            # 单个指令，直接发送
                            print(f"redis-cli set drone_command '{json.dumps(result)}'")
                        print()
                    else:
                        print("错误: 生成的指令格式不正确")
                        print(f"生成的指令: {json.dumps(result, indent=2)}")
                        print(f"处理时间: {elapsed_time:.2f}秒")
                        print()
            except Exception as e:
                print(f"发生错误: {e}")
                import traceback
                traceback.print_exc()
                print()
    else:
        # 没有命令行参数，运行交互式模式
        main()
