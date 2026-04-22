import subprocess
import time

# 测试命令
test_commands = [
    "起飞到2米，然后向前飞1米，最后降落",
    "向前移动0.5米",
    "移动到坐标(5,3,2)",
    "悬停",
    "exit"
]

# 启动无人机指令解析器进程
process = subprocess.Popen(
    ["D:/conda_envs/ollama/python.exe", "drone_command_parser.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding='utf-8'
)

# 等待程序启动
time.sleep(1)

# 读取初始输出
try:
    initial_output = process.stdout.readline()
    print(initial_output, end='')
    
    # 逐行读取并打印输出
    while True:
        line = process.stdout.readline()
        if not line:
            break
        print(line, end='')
        if "请输入无人机指令:" in line:
            # 输入测试命令
            if test_commands:
                command = test_commands.pop(0)
                print(f"输入: {command}")
                process.stdin.write(command + '\n')
                process.stdin.flush()
            else:
                break
    
    # 等待进程结束
    process.wait()
    
    # 读取剩余输出
    remaining_output = process.stdout.read()
    print(remaining_output, end='')
    
    # 读取错误输出
    error_output = process.stderr.read()
    if error_output:
        print("错误输出:")
        print(error_output)
except Exception as e:
    print(f"发生错误: {e}")
    process.terminate()
