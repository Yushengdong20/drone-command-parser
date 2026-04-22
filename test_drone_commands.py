import subprocess
import sys

# 测试指令列表
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
    "悬停",
    "exit"
]

# 运行无人机指令解析器
process = subprocess.Popen(
    ["D:\\conda_envs\\ollama\\python.exe", "drone_command_parser.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# 发送测试指令
output = []
for command in test_commands:
    process.stdin.write(command + '\n')
    process.stdin.flush()

# 读取输出
while True:
    line = process.stdout.readline()
    if not line:
        break
    output.append(line)
    print(line, end='')

# 等待进程结束
process.wait()

# 读取错误输出
error_output = process.stderr.read()
if error_output:
    print("\n错误输出:")
    print(error_output)
