import time
from ollama import chat
from ollama import ChatResponse
import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_parameters(params, test_commands):
    """测试不同参数组合的推理时间"""
    results = []
    
    for command in test_commands:
        prompt = f"""
将无人机指令转换为JSON：
指令：{command}
格式：
- 起飞：{{"action":"take_off","params":{{"height":高度}}}}
- 降落：{{"action":"land"}}
- 移动：{{"action":"direction_move","params":{{"orientation":"方向","distance":距离}}}}
- 目标移动：{{"action":"point_move","params":{{"coordinate_type":1,"coordinate":[x,y,z]}}}}
- 悬停：{{"action":"emergency_hover"}}
方向：up/down/left/right/forward/backward
只输出JSON。
"""
        
        start_time = time.time()
        try:
            response: ChatResponse = chat(
                model='qwen3.5',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
                options=params
            )
            end_time = time.time()
            elapsed = end_time - start_time
            
            # 提取并解析JSON
            output = response['message']['content'].strip()
            start_idx = output.find('{')
            end_idx = output.rfind('}')
            if start_idx != -1 and end_idx != -1:
                output = output[start_idx:end_idx+1]
            json.loads(output)
            
            results.append({
                'command': command,
                'time': elapsed,
                'success': True
            })
            logging.info(f"Command: '{command}' - Time: {elapsed:.2f}s")
        except Exception as e:
            end_time = time.time()
            elapsed = end_time - start_time
            results.append({
                'command': command,
                'time': elapsed,
                'success': False,
                'error': str(e)
            })
            logging.error(f"Command: '{command}' - Error: {str(e)}")
    
    # 计算平均时间
    successful_times = [r['time'] for r in results if r['success']]
    if successful_times:
        avg_time = sum(successful_times) / len(successful_times)
        success_rate = len(successful_times) / len(results) * 100
    else:
        avg_time = float('inf')
        success_rate = 0
    
    return {
        'params': params,
        'results': results,
        'average_time': avg_time,
        'success_rate': success_rate
    }

def main():
    # 测试指令
    test_commands = [
        "起飞到2米高度",
        "降落",
        "向前移动1米",
        "向左移动0.5米",
        "移动到坐标(5,3,2)"
    ]
    
    # 测试不同参数组合
    parameter_sets = [
        # 基础参数（当前配置）
        {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.1,
            'top_p': 0.7,
            'max_new_tokens': 50
        },
        # 降低temperature
        {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.0,
            'top_p': 0.7,
            'max_new_tokens': 50
        },
        # 降低top_p
        {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.1,
            'top_p': 0.1,
            'max_new_tokens': 50
        },
        # 减少max_new_tokens
        {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.1,
            'top_p': 0.7,
            'max_new_tokens': 20
        },
        # 组合优化
        {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.0,
            'top_p': 0.1,
            'max_new_tokens': 20
        }
    ]
    
    # 运行测试
    all_results = []
    for i, params in enumerate(parameter_sets):
        print(f"\n测试参数组合 {i+1}/{len(parameter_sets)}")
        print(f"参数: {json.dumps(params, indent=2)}")
        result = test_parameters(params, test_commands)
        all_results.append(result)
        print(f"平均时间: {result['average_time']:.2f}s")
        print(f"成功率: {result['success_rate']:.1f}%")
    
    # 找出最佳参数
    best_result = min(all_results, key=lambda x: x['average_time'])
    print(f"\n最佳参数组合:")
    print(f"平均时间: {best_result['average_time']:.2f}s")
    print(f"成功率: {best_result['success_rate']:.1f}%")
    print(f"参数: {json.dumps(best_result['params'], indent=2)}")

if __name__ == "__main__":
    main()