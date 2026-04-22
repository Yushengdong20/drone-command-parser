import json
from a_model_wrapper import get_model_output

# 默认提示词
DEFAULT_PROMPT = '''
    你是无人机飞行指令解析器，将自然语言指令转换为严格的JSON格式。

    指令：{text_command}

    请按照以下格式输出：
    所有动作都包裹在数组中：[{{"action":"动作名称","params":{{...}}}}]
    多个动作：[{{"action":"动作1","params":{{...}}}},{{"action":"动作2","params":{{...}}}},...]

    动作列表：
    take_off: {{"action":"take_off","params":{{"height": 高度(米)}}}}
    land: {{"action":"land"}}
    direction_move: {{"action":"direction_move","params":{{"orientation": "up|down|left|right|forward|backward", "distance": 距离(米)}}}}
    yaw_change: {{"action":"yaw_change","params":{{"mode": "turn_to|turn_by", "angle": 角度(度), "speed": 角速度(度/秒,可选)}}}}
    emergency_hover: {{"action":"emergency_hover"}}
    turn_to: 转到指定方向（绝对角度，0°正北，90°正东，180°正南，270°正西）
    turn_by: 相对当前朝向转多少度（正值顺时针/右转，负值逆时针/左转）

    示例：
    输入：起飞
    输出：[{{"action":"take_off","params":{{"height":1.0}}}}]

    输入：降落
    输出：[{{"action":"land"}}]

    输入：向前2m
    输出：[{{"action":"direction_move","params":{{"orientation":"forward","distance":2.0}}}}]

    输入：升高2m
    输出：[{{"action":"direction_move","params":{{"orientation":"up","distance":2.0}}}}]

    输入：起飞，向前2m，然后降落
    输出：[{{"action":"take_off","params":{{"height":1.0}}}},{{"action":"direction_move","params":{{"orientation":"forward","distance":2.0}}}},{{"action":"land"}}]

    输入：起飞，向前2m，升高2m,降落
    输出：[{{"action":"take_off","params":{{"height":1.0}}}},{{"action":"direction_move","params":{{"orientation":"forward","distance":2.0}}}},{{"action":"direction_move","params":{{"orientation":"up","distance":2.0}}}},{{"action":"land"}}]

    输入：机头朝东
    输出：[{{"action":"yaw_change","params":{{"mode":"turn_to","angle":90.0}}}}]

    输入：向左转45度
    输出：[{{"action":"yaw_change","params":{{"mode":"turn_by","angle":-45.0}}}}]

    输入：顺时针转30度
    输出：[{{"action":"yaw_change","params":{{"mode":"turn_by","angle":30.0}}}}]

    输入：原地转一圈
    输出：[{{"action":"yaw_change","params":{{"mode":"turn_by","angle":360.0}}}}]

    输入：起飞，转向正南，然后降落
    输出：[{{"action":"take_off","params":{{"height":1.0}}}},{{"action":"yaw_change","params":{{"mode":"turn_to","angle":180.0}}}},{{"action":"land"}}]

    输入：悬停
    输出：[{{"action":"emergency_hover"}}]

    输入：停止
    输出：[{{"action":"emergency_hover"}}]

    输入：立即悬停
    输出：[{{"action":"emergency_hover"}}]

    输入：紧急停止
    输出：[{{"action":"emergency_hover"}}]

    输入：保持当前位置
    输出：[{{"action":"emergency_hover"}}]

    输入：暂停任务
    输出：[{{"action":"emergency_hover"}}]

    输入：原地等待
    输出：[{{"action":"emergency_hover"}}]

    请严格按照示例格式输出，只输出JSON，不要有任何解释或其他内容。
    '''


def process_model_output(model_output):
    """
    处理模型输出，确保返回有效的JSON
    
    Args:
        model_output (str): 模型输出的原始内容
    
    Returns:
        dict or list: 解析后的JSON对象或数组
    """
    try:
        # 清理输出
        model_output = model_output.strip()
        
        # 处理```json ```格式
        if model_output.startswith('```json') and model_output.endswith('```'):
            model_output = model_output[7:-3].strip()
        
        # 检查是否是复合指令（多个JSON对象用逗号连接）
        if '},{' in model_output:
            # 如果是复合指令，添加方括号使其成为合法的JSON数组
            model_output = '[' + model_output + ']'
        
        # 解析JSON
        command_json = json.loads(model_output)
        
        # 处理可能的嵌套数组
        if isinstance(command_json, list) and len(command_json) == 1 and isinstance(command_json[0], list):
            command_json = command_json[0]
        
        return command_json
    except json.JSONDecodeError as e:
        return {"error": "解析指令失败", "details": str(e)}


def send_to_redis(command):
    """
    模拟发送指令到Redis
    
    Args:
        command (dict or list): 要发送的指令
    """
    if isinstance(command, list):
        # 复合指令，逐一发送
        for i, cmd in enumerate(command):
            print(f"步骤 {i+1}: redis-cli set drone_command '{json.dumps(cmd)}'")
    else:
        # 单个指令，直接发送
        print(f"redis-cli set drone_command '{json.dumps(command)}'")


def test_single_command(command_text, model="qwen3.5", options=None, prompt=None):
    """
    测试单个指令
    
    Args:
        command_text (str): 指令文本
        model (str): 模型名称
        options (dict): 模型配置
        prompt (str): 提示词模板
    """
    print(f"测试指令: {command_text}")
    
    # 获取模型输出
    model_output, elapsed_time = get_model_output(command_text, model, options, prompt)
    print(f"模型输出: {model_output}")
    print(f"处理时间: {elapsed_time:.2f}秒")
    
    # 处理模型输出
    processed_output = process_model_output(model_output)
    
    # 检查是否有错误
    if isinstance(processed_output, dict) and "error" in processed_output:
        print(f"错误: {processed_output['error']}")
        if "details" in processed_output:
            print(f"详情: {processed_output['details']}")
    else:
        # 打印处理后的输出
        print("处理后的指令:")
        print(json.dumps(processed_output, indent=2))
        
        # 模拟发送到Redis
        print("\n模拟发送到Redis:")
        send_to_redis(processed_output)
    
    print("-----------------")


if __name__ == "__main__":
    options = {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            # 'num_ctx': 4096,
            'num_ctx': 16384,
            'temperature': 1.0,
            'top_p': 0.1,
            'max_new_tokens': 500
        }
# 测试单个指令
    print(f"使用提示词：\n{DEFAULT_PROMPT}")
    print(f"使用模型配置：\n{options}")
    # test_single_command("起飞", prompt=DEFAULT_PROMPT, options=options)
    # test_single_command("降落", prompt=DEFAULT_PROMPT, options=options)
    # test_single_command("向后2m", prompt=DEFAULT_PROMPT, options=options)
    test_single_command("悬停", prompt=DEFAULT_PROMPT, options=options)

    # 测试复合指令
    # test_single_command("起飞，向后2m，然后降落", prompt=DEFAULT_PROMPT, options=options)
    # test_single_command("起飞到2米，然后向前飞1米，最后降落", prompt=DEFAULT_PROMPT, options=options)
