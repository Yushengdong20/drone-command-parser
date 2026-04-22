import json
import time
import sys
from a_model_wrapper import get_model_output
from b_test_script import process_model_output, DEFAULT_PROMPT, send_to_redis

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# 重定向标准输出到日志文件
sys.stdout = Logger("c_report.md")


def run_test_with_expectations(test_cases, model="qwen3.5", options=None, prompt=None):
    """
    运行测试，评估测试指令与期待输出是否一致
    
    Args:
        test_cases (dict): 测试指令集合，键为自然语言指令，值为期待的大模型输出
        model (str): 模型名称
        options (dict): 模型配置
        prompt (str): 提示词模板
    
    Returns:
        tuple: (total_time, results)
            total_time: 本轮测试总耗时
            results: 测试结果，包含每个测试用例的详细信息
    """
    # 默认提示词
    if prompt is None:
        prompt = DEFAULT_PROMPT
    
    # 运行测试
    print("无人机指令解析器测试")
    print("=" * 60)
    print("开始测试...")
    print("=" * 60)
    
    start_time = time.time()
    results = []
    
    for command, expected_output in test_cases.items():
        print(f"\n测试指令: {command}")
        print(f"期待输出: {expected_output}")
        
        # 获取模型输出
        model_output, elapsed_time = get_model_output(command, model, options, prompt)
        print(f"模型输出: {model_output}")
        print(f"处理时间: {elapsed_time:.2f}秒")
        
        # 处理模型输出
        processed_output = process_model_output(model_output)
        
        # 检查是否有错误
        if isinstance(processed_output, dict) and "error" in processed_output:
            print(f"错误: {processed_output['error']}")
            if "details" in processed_output:
                print(f"详情: {processed_output['details']}")
            match = False
        else:
            # 打印处理后的输出
            print("处理后的指令:")
            print(json.dumps(processed_output, indent=2))
            
            # 评估是否与期待输出一致
            try:
                expected_json = json.loads(expected_output)
                match = processed_output == expected_json
                print(f"与期待输出匹配: {'✓' if match else '✗'}")
            except json.JSONDecodeError:
                print("错误: 期待输出不是有效的JSON格式")
                match = False
            
            # 模拟发送到Redis
            print("\n模拟发送到Redis:")
            send_to_redis(processed_output)
        
        # 存储结果
        results.append({
            "command": command,
            "expected_output": expected_output,
            "model_output": model_output,
            "processed_output": processed_output,
            "elapsed_time": elapsed_time,
            "match": match
        })
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print(f"总测试时间: {total_time:.2f}秒")
    
    # 计算匹配率
    matched_count = sum(1 for result in results if result['match'])
    total_count = len(results)
    match_rate = (matched_count / total_count) * 100 if total_count > 0 else 0
    print(f"匹配率: {match_rate:.2f}% ({matched_count}/{total_count})")
    print("=" * 60)
    
    return total_time, results


if __name__ == "__main__":
    # 示例测试用例
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
    
    # 运行测试
    total_time, results = run_test_with_expectations(test_cases)
    
    # 打印详细结果
    print("\n详细测试结果:")
    for result in results:
        print(f"\n指令: {result['command']}")
        print(f"匹配: {'✓' if result['match'] else '✗'}")
        print(f"耗时: {result['elapsed_time']:.2f}秒")

