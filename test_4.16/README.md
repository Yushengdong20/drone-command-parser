# 无人机指令解析器测试脚本

## 目录结构

```
test/
├── a_model_wrapper.py  # 模型封装脚本
├── b_test_script.py    # 简单测试脚本
├── c_single_test.py    # 单次测试脚本（支持自定义提示词）
├── d_interactive_test.py  # 交互式测试脚本
├── e_performance.py    # 性能测试脚本
└── README.md          # 说明文档
```

## 脚本说明

### 1. a_model_wrapper.py

**功能**：封装Ollama模型调用，提供统一的接口获取模型输出。

**主要函数**：
- `get_model_output(text_command, model="qwen3.5", options=None, prompt=None)`: 调用Ollama模型获取输出
  - `text_command`: 输入的指令文本
  - `model`: 使用的模型名称（默认为"qwen3.5"）
  - `options`: 模型配置参数（默认使用推荐配置）
  - `prompt`: 提示词模板，如果为None则使用默认模板
  - 返回值: (model_output, elapsed_time)，其中model_output是模型输出的原始内容，elapsed_time是处理时间

### 2. b_test_script.py

**功能**：配置模型参数，调用a脚本获取模型输出，处理输出内容，并模拟发送到Redis。

**主要函数**：
- `process_model_output(model_output)`: 处理模型输出，确保返回有效的JSON
- `send_to_redis(command)`: 模拟发送指令到Redis（只打印在终端）
- `test_single_command(command_text, model="qwen3.5", options=None, prompt=None)`: 测试单个指令
  - `command_text`: 指令文本
  - `model`: 模型名称（默认为"qwen3.5"）
  - `options`: 模型配置参数
  - `prompt`: 提示词模板

**使用方法**：
```python
# 测试单个指令
test_single_command("起飞")
test_single_command("降落")
test_single_command("向后2m")

# 测试复合指令
test_single_command("起飞，向后2m，然后降落")
test_single_command("起飞到2米，然后向前飞1米，最后降落")

# 使用自定义提示词
custom_prompt = '''
请将以下指令转换为JSON格式：
{text_command}

示例：
起飞 -> {{"action":"take_off","params":{{"height":1.0}}}}
降落 -> {{"action":"land"}}

只输出JSON，不要有其他内容。
'''
test_single_command("起飞", prompt=custom_prompt)
```

### 3. c_performance_test.py

**功能**：比较不同模型和配置的性能，生成性能测试报告。

**主要函数**：
- `run_performance_test()`: 运行性能测试，比较不同模型和配置的性能
- `generate_report(test_results)`: 生成性能测试报告

**测试配置**：
- qwen3.5:9b (默认配置)
- qwen3.5:0.8b (默认配置)
- qwen3.5:9b (高温度)
- qwen3.5:9b (大上下文)

**测试指令**：
- "起飞"
- "降落"
- "向后2m"
- "起飞，向后2m，然后降落"
- "起飞到2米，然后向前飞1米，最后降落"

## 使用示例

### 1. 运行简单测试

```bash
# 进入test目录
cd test

# 运行b_test_script.py
python b_test_script.py
```

### 2. 运行单次测试（支持自定义提示词）

```bash
# 进入test目录
cd test

# 运行c_single_test.py
python c_single_test.py
```

### 3. 运行交互式测试

```bash
# 进入test目录
cd test

# 运行d_interactive_test.py
python d_interactive_test.py

# 输入指令进行测试，输入 'exit' 退出，输入 'prompt' 查看或修改提示词
```

### 4. 运行性能测试

```bash
# 进入test目录
cd test

# 运行e_performance.py
python e_performance.py

# 查看性能测试报告
cat performance_report.md
```

## 注意事项

1. 确保已经安装了ollama模块：`pip install ollama`
2. 确保已经下载了相应的模型：
   - `ollama pull qwen3.5:9b`
   - `ollama pull qwen3.5:0.8b`
3. 性能测试可能需要较长时间，请耐心等待
4. 生成的性能测试报告保存在`performance_report.md`文件中
