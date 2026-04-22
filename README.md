# 无人机指令解析器项目

## 项目概述

本项目使用本地部署的大模型（qwen3.5）来解析用户输入的自然语言指令，将其转换为标准化的JSON格式无人机飞行指令。这些指令可以直接发送到Redis，供无人机控制系统使用。

## 文件结构

```
本地ollama格式化输出/
├── drone_command_parser.py  # 主解析器脚本
├── test_drone_commands.py   # 批量测试脚本
├── test_optimization.py     # 参数优化测试脚本
├── parameter_comparison_test.py  # 参数对比测试脚本
├── parameter_comparison_report.md  # 参数优化对比报告
├── test_report.md           # 性能测试报告
└── README.md                # 项目说明文档
```

## 文件功能说明

### 1. drone_command_parser.py

**核心功能**：
- 将自然语言指令转换为JSON格式
- 支持多种无人机指令类型
- 包含完整的错误处理和日志记录
- 实现了LRU缓存机制
- 支持多轮性能测试

**主要函数**：
- `generate_drone_command()`：核心函数，将文本指令转换为JSON格式
- `validate_command()`：验证生成的指令格式是否正确
- `run_test_round()`：运行一轮测试
- `generate_test_report()`：生成测试报告
- `main()`：交互式命令行界面

**技术参数**：
- 模型：qwen3.5 (Q4_K_M 量化版本)
- 上下文长度：2048
- GPU使用率：100% (通过 tensor_split 优化)
- 平均处理时间：约10.42秒
- 显存占用：约8.6GB
- 成功率：100%

### 2. test_drone_commands.py

**功能**：
- 自动测试多种指令类型
- 验证解析器功能的正确性
- 输出详细的测试结果

### 3. test_optimization.py

**功能**：
- 测试不同参数组合的推理时间
- 找出最佳参数配置
- 评估参数优化效果

**使用方法**：
```bash
python test_optimization.py
```

**测试内容**：
- 测试5种不同参数组合
- 评估temperature、top_p、max_new_tokens参数的影响
- 输出最佳参数配置

### 4. parameter_comparison_test.py

**功能**：
- 详细比较不同参数集的性能
- 生成参数优化对比报告
- 分析指令级性能差异

**使用方法**：
```bash
python parameter_comparison_test.py
```

**测试内容**：
- 测试4种参数配置（基准配置和3种优化配置）
- 生成详细的参数对比报告
- 分析每个指令在不同参数下的性能表现

### 5. parameter_comparison_report.md

**内容**：
- 不同参数集的性能对比
- 指令级性能分析
- 参数优化效果评估
- 详细的性能数据

### 6. test_report.md

**内容**：
- 多轮测试结果
- 系统稳定性分析
- 处理时间统计
- 技术参数汇总

## 支持的指令类型

| 指令类型 | 动作名称 | 参数说明 | 示例输入 | 生成的JSON |
|---------|---------|---------|---------|-----------|
| 起飞 | take_off | height: 起飞高度（米） | 起飞到2米高度 | `{"action":"take_off","params":{"height":2.0}}` |
| 降落 | land | 无参数 | 降落 | `{"action":"land"}` |
| 六向移动 | direction_move | orientation: 方向<br>distance: 距离（米，默认0.3） | 向前移动1米 | `{"action":"direction_move","params":{"orientation":"forward","distance":1.0}}` |
| 目标点移动 | point_move | coordinate_type: 坐标类型（1=相对，2=GPS）<br>coordinate: 坐标[x,y,z] | 移动到坐标(5,3,2) | `{"action":"point_move","params":{"coordinate_type":1,"coordinate":[5.0,3.0,2.0]}}` |
| 固定圆形航线持续盘旋 | fixed_Circle | coordinate_type: 坐标类型<br>point: 中心点坐标[x,y,z]<br>radius: 半径（米） | 以(15,10)为中心，半径5米盘旋 | `{"action":"fixed_Circle","params":{"coordinate_type":1,"point":[15.0,10.0,2.0],"radius":5.0}}` |
| 固定圆形航线单次盘旋 | fixed_Circle_1 | coordinate_type: 坐标类型<br>point: 中心点坐标[x,y,z]<br>radius: 半径（米） | 以(15,10)为中心，半径5米单次盘旋 | `{"action":"fixed_Circle_1","params":{"coordinate_type":1,"point":[15.0,10.0,2.0],"radius":5.0}}` |
| 悬停 | emergency_hover | 无参数 | 悬停 | `{"action":"emergency_hover"}` |

## 方向参数说明

| 方向 | 对应值 | 示例输入 |
|-----|-------|--------|
| 向上 | up | 向上移动1米 |
| 向下 | down | 向下移动1米 |
| 向左 | left | 向左移动0.5米 |
| 向右 | right | 向右移动0.5米 |
| 向前 | forward | 向前移动0.3米 |
| 向后 | backward | 向后移动0.3米 |

## 坐标类型说明

| 类型 | 对应值 | 格式 | 示例 |
|-----|-------|------|------|
| 相对坐标 | 1 | [x,y,z]（米） | [5.0,3.0,2.0] |
| GPS坐标 | 2 | [经度,纬度,高度] | [8.5456277,47.397951,537.3179011819127] |

## 最佳参数配置

```json
{
  "main_gpu": 0,
  "tensor_split": [1, 0],
  "num_ctx": 2048,
  "temperature": 0.0,
  "top_p": 0.1,
  "max_new_tokens": 20
}
```

**参数说明**：
- `main_gpu`: 指定使用主GPU
- `tensor_split`: 在GPU之间分配张量，优化内存使用
- `num_ctx`: 上下文长度，平衡性能和理解能力
- `temperature`: 生成温度，0.0表示完全确定性
- `top_p`: 采样参数，0.1表示最小搜索空间
- `max_new_tokens`: 最大输出 tokens 数，限制输出长度

## 性能测试结果

### 整体性能

| 指标 | 值 |
|-----|------|
| 平均处理时间 | 10.42秒 |
| 最快处理时间 | 5.67秒 |
| 最慢处理时间 | 13.72秒 |
| GPU使用率 | 100% |
| 成功率 | 100% |

### 指令级性能

| 指令 | 平均时间 (秒) | 提升幅度 |
|-----|---------------|----------|
| 起飞到2米高度 | 11.82 | +5.0% |
| 降落 | 5.67 | +28.0% |
| 向前移动1米 | 13.72 | -11.7% |
| 向后移动0.5米 | 8.80 | -1.6% |
| 向左移动0.3米 | 7.64 | -0.1% |
| 向右移动0.4米 | 12.79 | +46.6% |
| 向上移动0.8米 | 7.76 | +38.9% |
| 向下移动0.2米 | 13.21 | -30.4% |
| 移动到坐标(5,3,2) | 11.99 | +11.9% |
| 悬停 | 10.84 | +3.7% |

## 使用方法

### 环境准备

1. **安装Ollama**：从官方网站下载并安装Ollama
2. **部署qwen3.5模型**：`ollama pull qwen3.5`
3. **安装Python包**：`pip install ollama`

### 运行方式

#### 交互式模式

```bash
python drone_command_parser.py
```

输入示例：
```
请输入无人机指令: 起飞到2米高度
生成的指令:
{
  "action": "take_off",
  "params": {
    "height": 2
  }
}

模拟发送到Redis:
redis-cli set drone_command '{"action": "take_off", "params": {"height": 2}}'
```

#### 批量测试模式

```bash
python test_drone_commands.py
```

#### 性能测试

在交互式模式下输入 `test` 运行多轮性能测试：
```
请输入无人机指令: test
```

### 测试功能对比

| 特性 | test_drone_commands.py | drone_command_parser.py (输入test) |
|-----|----------------------|----------------------------------|
| 运行方式 | 自动批量测试 | 手动触发测试 |
| 输出方式 | 直接显示到控制台 | 生成详细的测试报告文件 |
| 测试轮数 | 1轮 | 3轮 |
| 报告生成 | 无 | 生成 test_report.md |
| 适合场景 | 快速验证功能 | 详细性能测试 |

## 优化建议

1. **保持当前配置**：当前参数组合已经达到了较好的性能平衡
2. **考虑模型替换**：如果需要进一步提升速度，可以考虑使用更小的模型如llama3.2:3b
3. **批量处理**：对于多个指令，可以考虑批量处理以减少模型加载开销
4. **缓存机制**：已实现LRU缓存，可进一步优化缓存策略
5. **提示模板优化**：可以根据实际使用情况调整提示模板，提高解析准确性

## 脚本产物文件对应关系

| 脚本文件 | 产物文件 | 说明 |
|---------|---------|------|
| drone_command_parser.py | test_report.md | 运行 `test` 命令时生成的性能测试报告 |
| test_optimization.py | 无固定产物 | 直接输出最佳参数配置到控制台 |
| parameter_comparison_test.py | parameter_comparison_report.md | 生成详细的参数对比报告 |
| test_drone_commands.py | 无固定产物 | 直接输出测试结果到控制台 |

## 注意事项

- 确保Ollama服务正在运行（默认端口11434）
- 输入指令应清晰明确，避免歧义
- 对于复杂指令，可能需要多次尝试以获得正确的解析结果
- 确保GPU驱动最新，以获得最佳性能

## 后续扩展

- **支持更多指令类型**：可在提示模板中添加新的指令类型
- **优化解析逻辑**：根据实际使用情况调整提示模板
- **增加参数验证**：对输入参数进行更严格的验证
- **添加API接口**：提供HTTP API接口供其他系统调用
- **支持多语言指令**：扩展支持英文等其他语言的指令解析