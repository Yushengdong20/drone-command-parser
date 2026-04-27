# 无人机指令解析器测试脚本

## 目录结构

```
├── a_model_wrapper.py      # 模型封装脚本
├── b_test_script.py        # 简单测试脚本
├── c_single_test.py        # 单次测试脚本（支持自定义提示词）
├── d_interactive_test.py   # 交互式测试脚本
├── e_performance.py        # 性能测试脚本（模型对比）
├── f_context_test.py       # 上下文大小测试脚本
├── g_temperature_test.py   # 温度参数测试脚本
├── h_top_p_test.py         # top_p参数测试脚本
├── i_top_k_test.py         # top_k参数测试脚本
├── k_redis_test.py         # Redis操作测试脚本
├── e_report/              # 性能测试报告目录
├── f_report/              # 上下文测试报告目录
├── g_report/              # 温度测试报告目录
├── h_report/              # top_p测试报告目录
├── i_report/              # top_k测试报告目录
├── LICENSE                # GPLv3 License文件
├── COMMERCIAL_LICENSE     # 商业使用许可证文件
└── README.md              # 说明文档
```

## 脚本说明

### 1. a\_model\_wrapper.py

**功能**：封装Ollama模型调用，提供统一的接口获取模型输出。

**主要函数**：

- `get_model_output(text_command, model="qwen3.5", options=None, prompt=None)`: 调用Ollama模型获取输出
  - `text_command`: 输入的指令文本
  - `model`: 使用的模型名称（默认为"qwen3.5"）
  - `options`: 模型配置参数（默认使用推荐配置）
  - `prompt`: 提示词模板，如果为None则使用默认模板
  - 返回值: (model\_output, elapsed\_time)，其中model\_output是模型输出的原始内容，elapsed\_time是处理时间

**产出**：无直接产出，作为其他脚本的依赖模块。

### 2. b\_test\_script.py

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

**产出**：在终端输出测试结果和模拟的Redis命令。

### 3. c\_single\_test.py

**功能**：运行单次测试，评估测试指令与期待输出是否一致，并生成测试报告。

**主要函数**：

- `run_test_with_expectations(test_cases, model="qwen3.5", options=None, prompt=None)`: 运行测试，评估测试指令与期待输出是否一致
  - `test_cases`: 测试指令集合，键为自然语言指令，值为期待的大模型输出
  - `model`: 模型名称
  - `options`: 模型配置
  - `prompt`: 提示词模板
  - 返回值: (total\_time, results)，其中total\_time是本轮测试总耗时，results是测试结果

**测试用例**：包含43个测试指令，涵盖基础动作、航向控制、组合指令和边界情况。

**产出**：

- 在终端输出测试结果
- 生成 `c_report.md` 测试报告文件

### 4. d\_interactive\_test.py

**功能**：提供交互式测试界面，允许用户输入指令进行测试。

**使用方法**：

```bash
# 运行交互式测试
python d_interactive_test.py

# 输入指令进行测试，输入 'exit' 退出，输入 'prompt' 查看或修改提示词
```

**产出**：在终端输出测试结果和模拟的Redis命令。

### 5. e\_performance.py

**功能**：比较不同模型的性能，生成性能测试报告。

**测试配置**：

- qwen3.5:latest
- qwen3.5:0.8b

**主要函数**：

- `run_performance_test()`: 运行性能测试，比较不同模型的性能
- `generate_report(test_results, test_logs, report_filename, test_cases)`: 生成性能测试报告

**产出**：

- 在 `e_report` 目录中生成性能测试报告文件
- 报告文件会自动添加编号，避免覆盖之前的报告
- 示例：`performance_report_full.md`、`performance_report_full_001.md`

### 6. f\_context\_test.py

**功能**：比较不同上下文大小的性能，生成上下文测试报告。

**测试配置**：

- 高上下文 (16384)
- 低上下文 (2048)

**主要函数**：

- `run_context_test()`: 运行上下文大小测试，比较不同上下文大小的性能
- `generate_report(test_results, test_logs, report_filename, test_cases)`: 生成上下文测试报告

**产出**：

- 在 `f_report` 目录中生成上下文测试报告文件
- 报告文件会自动添加编号，避免覆盖之前的报告
- 示例：`context_test_report_full.md`、`context_test_report_full_001.md`

### 7. g\_temperature\_test.py

**功能**：比较不同温度参数的性能，生成温度测试报告。

**测试配置**：

- 温度 0.0
- 温度 0.3
- 温度 0.7
- 温度 1.0

**主要函数**：

- `run_temperature_test()`: 运行温度参数测试，比较不同温度对性能的影响
- `generate_report(test_results, test_logs, report_filename, test_cases)`: 生成温度测试报告

**产出**：

- 在 `g_report` 目录中生成温度测试报告文件
- 报告文件会自动添加编号，避免覆盖之前的报告
- 示例：`temperature_test_report_full.md`、`temperature_test_report_full_001.md`

## 使用示例

### 1. 运行简单测试

```bash
# 运行b_test_script.py
python b_test_script.py
```

### 2. 运行单次测试（支持自定义提示词）

```bash
# 运行c_single_test.py
python c_single_test.py

# 查看测试报告
cat c_report.md
```

### 3. 运行交互式测试

```bash
# 运行d_interactive_test.py
python d_interactive_test.py

# 输入指令进行测试，输入 'exit' 退出，输入 'prompt' 查看或修改提示词
```

### 4. 运行性能测试（模型对比）

```bash
# 运行e_performance.py
python e_performance.py

# 查看性能测试报告
ls e_report/
cat e_report/performance_report_full.md
```

### 5. 运行上下文大小测试

```bash
# 运行f_context_test.py
python f_context_test.py

# 查看上下文测试报告
ls f_report/
cat f_report/context_test_report_full.md
```

### 6. 运行温度参数测试

```bash
# 运行g_temperature_test.py
python g_temperature_test.py

# 查看温度测试报告
ls g_report/
cat g_report/temperature_test_report_full.md
```

### 7. 运行 top\_p 参数测试

```bash
# 运行h_top_p_test.py
python h_top_p_test.py

# 查看 top_p 测试报告
ls h_report/
cat h_report/top_p_test_report_full.md
```

### 8. 运行 top\_k 参数测试

```bash
# 运行i_top_k_test.py
python i_top_k_test.py

# 查看 top_k 测试报告
ls i_report/
cat i_report/top_k_test_report_full.md
```

## 注意事项

1. 确保已经安装了ollama模块：`pip install ollama`
2. 确保已经下载了相应的模型：
   - `ollama pull qwen3.5:latest`
   - `ollama pull qwen3.5:0.8b`
   - `ollama pull qwen3.5:2b`
   - `ollama pull qwen3.5:4b`
3. 性能测试可能需要较长时间，请耐心等待
4. 生成的测试报告保存在各自的报告目录中
5. 报告文件会自动添加编号，避免覆盖之前的报告
6. 使用conda环境：`conda activate ollama`

## 许可证

本项目采用双许可证模式：

1. **个人和非商业使用**：使用 GPLv3 License，免费开源
2. **商业使用**：需要联系作者获取商业许可证，可能需要支付费用

### 联系方式

- 邮箱：<992456388@qq.com>
- GitHub：Sheldon-Yu

### 许可证文件

- [LICENSE](LICENSE)：GPLv3 License 详细文本
- [COMMERCIAL\_LICENSE](COMMERCIAL_LICENSE)：商业使用许可证详细条款

