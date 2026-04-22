import json
from b_test_script import test_single_command, DEFAULT_PROMPT


def run_interactive_test():
    """
    运行交互式测试，不断循环直到输入exit或者ctrl+c退出
    """
    # 默认配置
    options = {
        'main_gpu': 0,
        'tensor_split': [1, 0],
        # 'num_ctx': 2048,
        'num_ctx': 4096,
        'temperature': 0.0,
        'top_p': 0.1,
        'max_new_tokens': 500
    }
    
    # 默认提示词
    current_prompt = DEFAULT_PROMPT
    
    # 打印提示
    print("无人机指令解析器交互式测试")
    print("输入 'exit' 退出程序")
    print("输入 'prompt' 查看或修改提示词")
    print("=" * 60)
    
    while True:
        try:
            # 获取用户输入
            user_input = input("请输入无人机指令: ")
            
            # 处理特殊命令
            if user_input.lower() == 'exit':
                print("程序退出")
                break
            elif user_input.lower() == 'prompt':
                print("当前提示词模板:")
                print(current_prompt)
                print("=" * 60)
                use_custom = input("是否修改提示词？(y/n): ").lower()
                if use_custom == 'y':
                    print("请输入新的提示词模板（{text_command}将被替换为指令文本）:")
                    current_prompt = input()
                continue
            
            # 运行测试
            test_single_command(user_input, prompt=current_prompt, options=options)
            
        except KeyboardInterrupt:
            print("\n程序退出")
            break


if __name__ == "__main__":
    run_interactive_test()
