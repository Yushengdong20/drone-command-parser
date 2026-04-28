# 无人机指令解析器测试脚本

## 目录结构

```
├── a_model_wrapper.py      # 模型封装脚本
├── b_test_script.py        # 简单测试脚本（支持Redis队列）
├── c_single_test.py        # 单次测试脚本（支持自定义提示词）
├── d_interactive_test.py   # 交互式测试脚本
├── e_performance.py        # 性能测试脚本（模型对比）
├── f_context_test.py       # 上下文大小测试脚本
├── g_temperature_test.py   # 温度参数测试脚本
├── h_top_p_test.py         # top_p参数测试脚本
├── i_top_k_test.py         # top_k参数测试脚本
├── k_redis_writer.py       # Redis队列写入脚本
├── l_redis_reader.py       # Redis队列读取脚本
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

### 1. a_model_wrapper.py

**功能**：封装Ollama模型调用，提供统一的接口获取模型输出。

**主要函数**：

- `get_model_output(text_command, model="qwen3.5", options=None, prompt=None)`: 调用Ollama模型获取输出
  - `text_command`: 输入的指令文本
  - `model`: 使用的模型名称（默认为"qwen3.5"）
  - `options`: 模型配置参数（默认使用推荐配置）
  - `prompt`: 提示词模板，如果为None则使用默认模板
  - 返回值: (model_output, elapsed_time)，其中model_output是模型输出的原始内容，elapsed_time是处理时间

**产出**：无直接产出，作为其他脚本的依赖模块。

### 2. b_test_script.py

**功能**：配置模型参数，调用a脚本获取模型输出，处理输出内容，并发送到Redis队列（FIFO）。

**主要函数**：

- `process_model_output(model_output)`: 处理模型输出，确保返回有效的JSON
- `send_to_redis(command)`: 将指令发送到Redis队列（FIFO顺序）
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

# 测试复合指令（自动拆分为多个指令）
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

**产出**：在终端输出测试结果和Redis队列操作状态。

### 3. c_single_test.py

**功能**：运行单次测试，评估测试指令与期待输出是否一致，并生成测试报告。

**主要函数**：

- `run_test_with_expectations(test_cases, model="qwen3.5", options=None, prompt=None)`: 运行测试，评估测试指令与期待输出是否一致
  - `test_cases`: 测试指令集合，键为自然语言指令，值为期待的大模型输出
  - `model`: 模型名称
  - `options`: 模型配置
  - `prompt`: 提示词模板
  - 返回值: (total_time, results)，其中total_time是本轮测试总耗时，results是测试结果

**测试用例**：包含43个测试指令，涵盖基础动作、航向控制、组合指令和边界情况。

**产出**：

- 在终端输出测试结果
- 生成 `c_report.md` 测试报告文件

### 4. d_interactive_test.py

**功能**：提供交互式测试界面，允许用户输入指令进行测试。

**使用方法**：

```bash
# 运行交互式测试
python d_interactive_test.py

# 输入指令进行测试，输入 'exit' 退出，输入 'prompt' 查看或修改提示词
```

**产出**：在终端输出测试结果和模拟的Redis命令。

### 5. e_performance.py

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

### 6. f_context_test.py

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

### 7. g_temperature_test.py

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

### 8. h_top_p_test.py

**功能**：测试不同top_p参数对模型输出的影响，生成测试报告。

**测试配置**：

- top_p 0.1
- top_p 0.5
- top_p 0.9
- top_p 1.0

**产出**：

- 在 `h_report` 目录中生成top_p测试报告文件
- 示例：`top_p_test_report_full.md`

### 9. i_top_k_test.py

**功能**：测试不同top_k参数对模型输出的影响，生成测试报告。

**测试配置**：

- top_k 10
- top_k 50
- top_k 100
- top_k 200

**产出**：

- 在 `i_report` 目录中生成top_k测试报告文件
- 示例：`top_k_test_report_full.md`

### 10. k_redis_writer.py

**功能**：模拟将大模型输出的指令添加到Redis队列（FIFO）。

**特点**：

- 模拟大模型输出的无人机指令
- 按照FIFO顺序添加到Redis队列
- 每条指令包含完整的元数据（command、timestamp、sequence）

**使用方法**：

```bash
# 运行Redis队列写入脚本
python k_redis_writer.py

# 注意：需要先安装redis模块和启动Redis服务器
```

**产出**：在终端显示添加过程和队列状态。

### 11. l_redis_reader.py

**功能**：从Redis队列中读取指令（FIFO顺序），验证队列功能。

**特点**：

- 按FIFO顺序读取队列中的指令
- 显示队列状态和内容
- 模拟指令处理过程
- 验证读取顺序与添加顺序一致

**使用方法**：

```bash
# 运行Redis队列读取脚本
python l_redis_reader.py

# 注意：需要先安装redis模块和启动Redis服务器
```

**产出**：在终端显示读取过程和处理结果。

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

### 7. 运行 top_p 参数测试

```bash
# 运行h_top_p_test.py
python h_top_p_test.py

# 查看 top_p 测试报告
ls h_report/
cat h_report/top_p_test_report_full.md
```

### 8. 运行 top_k 参数测试

```bash
# 运行i_top_k_test.py
python i_top_k_test.py

# 查看 top_k 测试报告
ls i_report/
cat i_report/top_k_test_report_full.md
```

### 9. 运行 Redis 队列写入

```bash
# 运行k_redis_writer.py
python k_redis_writer.py

# 注意：需要先安装redis模块和启动Redis服务器
pip install redis
```

### 10. 运行 Redis 队列读取

```bash
# 运行l_redis_reader.py
python l_redis_reader.py

# 注意：需要先安装redis模块和启动Redis服务器
```

### 11. 完整测试流程

```bash
# 1. 使用conda环境
conda activate ollama

# 2. 运行b_test_script.py生成指令并添加到队列
python b_test_script.py

# 3. 运行l_redis_reader.py从队列读取指令
python l_redis_reader.py

# 4. 验证FIFO顺序是否正确
```

## 核心功能

### 指令解析
- 将自然语言指令转换为严格的JSON格式
- 支持复合指令自动拆分（如"起飞，向前2m，然后降落"）
- 支持多种动作类型：take_off、land、direction_move、yaw_change、emergency_hover

### Redis队列
- 使用Redis队列实现FIFO（先进先出）机制
- 支持批量指令存储和顺序读取
- 每条指令包含时间戳和序列号，确保顺序正确

### 测试框架
- 支持多种参数测试：温度、top_p、top_k、上下文大小
- 自动生成测试报告
- 支持自定义提示词和模型配置

## 注意事项

1. 确保已经安装了ollama模块：`pip install ollama`
2. 确保已经下载了相应的模型：
   - `ollama pull qwen3.5:latest`
   - `ollama pull qwen3.5:0.8b`
   - `ollama pull qwen3.5:2b`
   - `ollama pull qwen3.5:4b`
3. Redis相关脚本需要：
   - 安装redis模块：`pip install redis`
   - 安装并启动Redis服务器（下载地址：https://redis.io/download）
4. 性能测试可能需要较长时间，请耐心等待
5. 生成的测试报告保存在各自的报告目录中
6. 报告文件会自动添加编号，避免覆盖之前的报告
7. 使用conda环境：`conda activate ollama`

## 许可证

本项目采用双许可证模式：

1. **个人和非商业使用**：使用 GPLv3 License，免费开源
2. **商业使用**：需要联系作者获取商业许可证，可能需要支付费用

### 联系方式

- 邮箱：<992456388@qq.com>
- GitHub：Sheldon-Yu

### 许可证文件

- [LICENSE](LICENSE)：GPLv3 License 详细文本
- [COMMERCIAL_LICENSE](COMMERCIAL_LICENSE)：商业使用许可证详细条款