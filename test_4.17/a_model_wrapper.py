from ollama import chat
from ollama import ChatResponse
import time


def get_model_output(text_command, model="qwen3.5", options=None, prompt=None):
    """
    调用Ollama模型获取输出
    
    Args:
        text_command (str): 输入的指令文本
        model (str): 使用的模型名称
        options (dict): 模型配置参数
        prompt (str): 提示词模板，如果为None则使用默认模板
    
    Returns:
        tuple: (model_output, elapsed_time)
    """
    # 默认配置
    if options is None:
        options = {
            'main_gpu': 0,
            'tensor_split': [1, 0],
            'num_ctx': 2048,
            'temperature': 0.0,
            'top_p': 0.1,
            'max_new_tokens': 500
        }
    
    # 定义提示模板
    if prompt is None:
        prompt = '''{text_command}'''.format(text_command=text_command)
    else:
        prompt = prompt.format(text_command=text_command)
    
    try:
        start_time = time.time()
        response: ChatResponse = chat(
            model=model, 
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
            options=options
        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        model_output = response['message']['content']
        return model_output, elapsed_time
    except Exception as e:
        return f"Error: {str(e)}", 0
