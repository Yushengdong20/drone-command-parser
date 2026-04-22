import json
import time
import subprocess
import os

# 设置环境变量，强制使用GPU
os.environ['OLLAMA_GPU_LAYER'] = 'cuda'

from c_single_test import run_test_with_expectations
from b_test_script import DEFAULT_PROMPT


def get_gpu_info():
    """
    获取GPU信息
    """
    try:
        # 使用nvidia-smi获取GPU信息
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name', '--format=csv,noheader'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        return 'Unknown GPU'
    except Exception as e:
        return 'Unknown GPU'


def run_top_k_test():
    """
    运行top_k参数测试，比较不同top_k对性能的影响
    """
    # 测试模式：True 为快速测试（只测试少量指令），False 为完整测试
    quick_test = False

    # 测试用例：键为自然语言指令，值为期待的大模型输出
    if quick_test:
        # 快速测试：只测试少量指令
        test_cases = {
            # 基础动作 - 起飞降落
            "起飞": '[{"action":"take_off","params":{"height":1.0}}]',
            "降落": '[{"action":"land"}]',
            # 基础动作 - 方向移动
            "向前2m": '[{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]',
            # 组合指令 - 简单序列
            "起飞，向前2m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]',
        }
    else:
        # 完整测试：测试所有指令
        test_cases = {
            # 基础动作 - 起飞降落
            "起飞": '[{"action":"take_off","params":{"height":1.0}}]',
            "降落": '[{"action":"land"}]',
            "起飞到2米": '[{"action":"take_off","params":{"height":2.0}}]',
            "起飞到5米": '[{"action":"take_off","params":{"height":5.0}}]',

            # 基础动作 - 方向移动
            "向前2m": '[{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]',
            "向后3m": '[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]',
            "向左1m": '[{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]',
            "向右5m": '[{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]',
            "升高2m": '[{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]',
            "降低1m": '[{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]',
            "向前飞10米": '[{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]',
            "往后退3米": '[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]',

            # 航向控制 - 绝对角度
            "机头朝北": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]',
            "机头朝东": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]',
            "机头朝南": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]',
            "机头朝西": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]',
            "转向正北": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]',
            "转向正东": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]',
            "转向正南": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]',
            "转向正西": '[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]',

            # 航向控制 - 相对角度
            "向左转45度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]',
            "向右转30度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]',
            "顺时针转90度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]',
            "逆时针转60度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]',
            "原地转一圈": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]',
            "左转90度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]',
            "右转180度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]',

            # 组合指令 - 简单序列
            "起飞，向前2m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]',
            "起飞，向后2m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]',
            "起飞，向左1m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]',
            "起飞，向右2m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]',

            # 组合指令 - 多步骤
            "起飞到2米，然后向前飞1米，最后降落": '[{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]',
            "起飞，升高2m，向前5m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]',
            "起飞，向前3m，向右2m，向后3m，向左2m，降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]',

            # 组合指令 - 含航向控制
            "起飞，转向正南，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]',
            "起飞，向前2m，向左转90度，再向前2m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]',
            "起飞，机头朝东，向前5m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]',
            "起飞，顺时针转180度，向前3m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]',

            # 复杂组合
            "起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落": '[{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]',
            "起飞，升高1m，原地转一圈，降低1m，然后降落": '[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]',

            # 边界情况
            "向前0.5m": '[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]',
            "起飞到0.5米": '[{"action":"take_off","params":{"height":0.5}}]',
            "向右转0度": '[{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]',
        }

    # 打印测试模式
    test_mode = '快速测试' if quick_test else '完整测试'
    print(f"测试模式: {test_mode}")
    print(f"测试指令数量: {len(test_cases)}")

    # 生成报告文件名
    import os
    report_suffix = '_quick' if quick_test else '_full'
    # 创建i_report目录（如果不存在）
    report_dir = 'i_report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # 获取GPU信息
    gpu_info = get_gpu_info()
    print(f"使用的GPU: {gpu_info}")
    
    # 添加编号逻辑，确保文件名唯一
    base_filename = f'top_k_test_report_{gpu_info.replace(" ", "_")}{report_suffix}'
    extension = '.md'
    counter = 1
    report_filename = os.path.join(report_dir, f'{base_filename}{extension}')
    
    # 检查文件是否存在，如果存在则添加编号
    while os.path.exists(report_filename):
        report_filename = os.path.join(report_dir, f'{base_filename}_{counter:03d}{extension}')
        counter += 1

    # 测试配置：只改变top_k，其他参数不变
    # 使用之前测试中最好的参数：qwen3.5:4b + 上下文 16384 + 温度 0.3
    test_configs = [
        {
            "name": "top_k 10",
            "top_k": 10
        },
        {
            "name": "top_k 20",
            "top_k": 20
        },
        {
            "name": "top_k 50",
            "top_k": 50
        },
        {
            "name": "top_k 100",
            "top_k": 100
        },
        {
            "name": "top_k 200",
            "top_k": 200
        }
    ]

    # 统一的模型和上下文配置
    model = "qwen3.5:4b"
    options_base = {
        'main_gpu': 0,
        'tensor_split': [1, 0],
        'num_ctx': 16384,  # 使用最佳上下文大小
        'temperature': 0.3,  # 使用最佳温度
        'max_new_tokens': 500
    }

    # 统一的提示词
    prompt = DEFAULT_PROMPT

    # 存储测试结果
    test_results = []
    # 存储测试日志
    test_logs = []
    # 按配置存储日志
    config_logs = {}

    # 运行测试
    for config in test_configs:
        test_name = config['name']
        top_k = config['top_k']

        # 复制基础配置并修改top_k
        options = options_base.copy()
        options['top_k'] = top_k

        print(f"\n=== 测试配置: {test_name} ===")
        test_logs.append(f"=== 测试配置: {test_name} ===")
        # 为每个配置创建单独的日志列表
        config_logs[test_name] = []

        # 捕获标准输出（同时在终端显示）
        import io
        import sys
        old_stdout = sys.stdout

        # 创建一个同时输出到终端和StringIO的对象
        class Tee:
            def __init__(self, terminal, string_io):
                self.terminal = terminal
                self.string_io = string_io

            def write(self, message):
                self.terminal.write(message)
                self.string_io.write(message)

            def flush(self):
                self.terminal.flush()
                self.string_io.flush()

        string_io = io.StringIO()
        sys.stdout = Tee(sys.stdout, string_io)

        # 运行测试
        total_time, results = run_test_with_expectations(test_cases, model=model, options=options, prompt=prompt)

        # 恢复标准输出
        sys.stdout = old_stdout
        captured_output = string_io.getvalue()

        # 添加捕获的输出到测试日志
        test_logs.extend(captured_output.splitlines())
        # 添加捕获的输出到配置日志
        config_logs[test_name].extend(captured_output.splitlines())

        # 存储结果
        config_results = {
            "name": test_name,
            "model": model,
            "options": options,
            "prompt": "DEFAULT_PROMPT",
            "total_time": total_time,
            "results": results
        }

        test_results.append(config_results)

        # 添加测试日志
        test_logs.append(f"总测试时间: {total_time:.2f}秒")
        matched_count = sum(1 for result in results if result['match'])
        total_count = len(results)
        match_rate = (matched_count / total_count) * 100 if total_count > 0 else 0
        test_logs.append(f"匹配率: {match_rate:.2f}% ({matched_count}/{total_count})")
        # 添加到配置日志
        config_logs[test_name].append(f"总测试时间: {total_time:.2f}秒")
        config_logs[test_name].append(f"匹配率: {match_rate:.2f}% ({matched_count}/{total_count})")

    # 生成报告
    generate_report(test_results, test_logs, config_logs, report_filename, test_cases, gpu_info)


def generate_report(test_results, test_logs, config_logs, report_filename, test_cases, gpu_info):
    """
    生成性能测试报告

    Args:
        test_results (list): 测试结果
        test_logs (list): 测试日志
        config_logs (dict): 按配置存储的日志
        report_filename (str): 报告文件名
        test_cases (dict): 测试用例
        gpu_info (str): GPU信息
    """
    report = "# 无人机指令解析器top_k参数测试报告\n\n"

    # 添加测试配置信息
    report += "## 测试配置\n\n"
    for config in test_results:
        report += f"### {config['name']}\n"
        report += f"- 模型: {config['model']}\n"
        report += f"- 提示词: {config['prompt']}\n"
        report += f"- 配置: {json.dumps(config['options'], indent=2)}\n\n"

    # 测试用例分类
    test_categories = {
        "基础动作 - 起飞降落": [
            "起飞", "降落", "起飞到2米", "起飞到5米"
        ],
        "基础动作 - 方向移动": [
            "向前2m", "向后3m", "向左1m", "向右5m", "升高2m", "降低1m", "向前飞10米", "往后退3米"
        ],
        "航向控制 - 绝对角度": [
            "机头朝北", "机头朝东", "机头朝南", "机头朝西", "转向正北", "转向正东", "转向正南", "转向正西"
        ],
        "航向控制 - 相对角度": [
            "向左转45度", "向右转30度", "顺时针转90度", "逆时针转60度", "原地转一圈", "左转90度", "右转180度"
        ],
        "组合指令 - 简单序列": [
            "起飞，向前2m，然后降落", "起飞，向后2m，然后降落", "起飞，向左1m，然后降落", "起飞，向右2m，然后降落"
        ],
        "组合指令 - 多步骤": [
            "起飞到2米，然后向前飞1米，最后降落", "起飞，升高2m，向前5m，然后降落", "起飞，向前3m，向右2m，向后3m，向左2m，降落"
        ],
        "组合指令 - 含航向控制": [
            "起飞，转向正南，然后降落", "起飞，向前2m，向左转90度，再向前2m，然后降落", "起飞，机头朝东，向前5m，然后降落", "起飞，顺时针转180度，向前3m，然后降落"
        ],
        "复杂组合": [
            "起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落", "起飞，升高1m，原地转一圈，降低1m，然后降落"
        ],
        "边界情况": [
            "向前0.5m", "起飞到0.5米", "向右转0度"
        ]
    }

    # 为每个分类生成表格
    report += "## 性能数据\n\n"
    all_results = []
    category_results = {}

    # 收集所有测试指令
    test_commands = set(test_cases.keys())

    # 只为包含测试指令的分类生成表格
    for category, commands in test_categories.items():
        # 检查该分类是否有测试指令
        category_commands = set(commands)
        common_commands = test_commands & category_commands

        if common_commands:
            # 只显示实际测试的指令
            actual_commands = sorted(common_commands)
            report += f"### {category}\n\n"
            # 构建表格头部
            header = "| 配置 | "
            for cmd in actual_commands:
                # 限制指令名称长度，避免表格过宽
                short_cmd = cmd[:10] + "..." if len(cmd) > 10 else cmd
                header += f"{short_cmd} |"
            header += " 分类总时间 | 分类匹配率 |\n"
            report += header
            # 构建表格分隔线
            separator = "|------|"
            for cmd in actual_commands:
                separator += "------|"
            separator += "----------|--------|\n"
            report += separator

            # 填充表格数据
            for config in test_results:
                row = f"| {config['name']} |"
                category_times = []
                category_matches = []

                for cmd in actual_commands:
                    for result in config['results']:
                        if result['command'] == cmd:
                            time_val = result['elapsed_time']
                            category_times.append(time_val)
                            category_matches.append(result['match'])
                            row += f" {time_val:.2f} |"
                            break

                category_total_time = sum(category_times)
                category_matched_count = sum(1 for match in category_matches if match)
                category_total_count = len(category_matches)
                category_match_rate = (category_matched_count / category_total_count) * 100 if category_total_count > 0 else 0
                row += f" {category_total_time:.2f} | {category_match_rate:.2f}% |\n"
                report += row

                # 存储分类结果
                if category not in category_results:
                    category_results[category] = {}
                category_results[category][config['name']] = {
                    "total_time": category_total_time,
                    "match_rate": category_match_rate,
                    "matched_count": category_matched_count,
                    "total_count": category_total_count
                }

    # 生成汇总表格
    report += "\n### 汇总\n\n"
    # 只为包含测试指令的分类生成汇总表格
    categories_with_tests = list(category_results.keys())

    if categories_with_tests:
        header = "| 配置 | "
        for category in categories_with_tests:
            # 限制分类名称长度，避免表格过宽
            short_category = category[:15] + "..." if len(category) > 15 else category
            header += f"{short_category} |"
        header += " 总时间 | 总匹配率 |\n"
        report += header

        separator = "|------|"
        for category in categories_with_tests:
            separator += "------|"
        separator += "----------|--------|\n"
        report += separator

        for config in test_results:
            row = f"| {config['name']} |"
            total_times = []
            total_matched = 0
            total_count = 0

            for category in categories_with_tests:
                cat_result = category_results[category].get(config['name'], {})
                cat_time = cat_result.get('total_time', 0)
                total_times.append(cat_time)
                total_matched += cat_result.get('matched_count', 0)
                total_count += cat_result.get('total_count', 0)
                row += f" {cat_time:.2f} |"

            overall_total_time = sum(total_times)
            overall_match_rate = (total_matched / total_count) * 100 if total_count > 0 else 0
            row += f" {overall_total_time:.2f} | {overall_match_rate:.2f}% |\n"
            report += row

            # 存储总体结果
            all_results.append({
                "name": config['name'],
                "total_time": overall_total_time,
                "match_rate": overall_match_rate,
                "matched_count": total_matched,
                "total_count": total_count
            })

    # 分析最佳配置
    best_time_result = min(all_results, key=lambda x: x['total_time'])
    max_accuracy = max(all_results, key=lambda x: x['match_rate'])['match_rate']
    best_accuracy_results = [result for result in all_results if result['match_rate'] == max_accuracy]

    # 添加性能总结
    report += "\n## 性能总结\n\n"
    for config in test_results:
        config_result = next((r for r in all_results if r['name'] == config['name']), None)
        if config_result:
            report += f"- {config['name']}: 总时间 = {config_result['total_time']:.2f}秒, 匹配率 = {config_result['match_rate']:.2f}% ({config_result['matched_count']}/{config_result['total_count']})\n"

    # 添加最佳配置分析
    report += "\n## 最佳配置分析\n\n"
    report += f"**最快配置**: {best_time_result['name']}\n"
    report += f"**总处理时间**: {best_time_result['total_time']:.2f}秒\n"
    report += f"**最高准确率配置**: {', '.join([r['name'] for r in best_accuracy_results])}\n"
    report += f"**匹配率**: {max_accuracy:.2f}%\n\n"

    # top_k对比分析
    report += "### top_k参数对比分析\n\n"
    for result in all_results:
        report += f"- {result['name']}: 总时间 = {result['total_time']:.2f}秒, 匹配率 = {result['match_rate']:.2f}% ({result['matched_count']}/{result['total_count']})\n"

    # 添加测试日志
    report += "\n## 测试日志\n\n"
    # 为每个测试配置生成单独的代码块
    for config, logs in config_logs.items():
        report += f"### {config}\n\n"
        report += "```text\n"
        report += f"使用的GPU: {gpu_info}\n\n"
        for log in logs:
            # 转义Markdown代码块标记，避免被解析为代码块
            log = log.replace('```', '\\`\\`\\`')
            report += log + "\n"
        report += "```\n\n"

    # 保存报告
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n性能测试报告已保存到: {report_filename}")
    print(f"\n最快配置: {best_time_result['name']}")
    print(f"总处理时间: {best_time_result['total_time']:.2f}秒")
    print(f"最高准确率配置: {', '.join([r['name'] for r in best_accuracy_results])}")
    print(f"匹配率: {max_accuracy:.2f}%")


if __name__ == "__main__":
    run_top_k_test()
