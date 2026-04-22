# 无人机指令解析器温度参数测试报告

## 测试配置

### 温度 0.0
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "temperature": 0.0
}

### 温度 0.3
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "temperature": 0.3
}

### 温度 0.7
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "temperature": 0.7
}

### 温度 1.0
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "temperature": 1.0
}

## 性能数据

### 基础动作 - 起飞降落

| 配置 | 起飞 |起飞到2米 |起飞到5米 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| 温度 0.0 | 2.65 | 2.81 | 2.86 | 1.96 | 10.29 | 100.00% |
| 温度 0.3 | 2.66 | 2.83 | 2.87 | 1.98 | 10.34 | 100.00% |
| 温度 0.7 | 2.65 | 2.79 | 2.83 | 1.96 | 10.24 | 100.00% |
| 温度 1.0 | 2.67 | 2.81 | 2.85 | 1.95 | 10.29 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 升高2m |向前2m |向前飞10米 |向右5m |向后3m |向左1m |往后退3米 |降低1m | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| 温度 0.0 | 2.81 | 2.78 | 1.94 | 2.68 | 2.06 | 2.18 | 2.82 | 2.44 | 19.71 | 100.00% |
| 温度 0.3 | 2.82 | 2.76 | 1.98 | 2.70 | 2.04 | 2.23 | 2.86 | 2.46 | 19.84 | 100.00% |
| 温度 0.7 | 2.79 | 2.75 | 1.96 | 2.69 | 2.05 | 2.22 | 2.37 | 2.42 | 19.25 | 100.00% |
| 温度 1.0 | 2.80 | 2.74 | 1.94 | 2.70 | 2.04 | 2.23 | 2.79 | 2.47 | 19.70 | 100.00% |
### 航向控制 - 绝对角度

| 配置 | 机头朝东 |机头朝北 |机头朝南 |机头朝西 |转向正东 |转向正北 |转向正南 |转向正西 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| 温度 0.0 | 2.82 | 4.97 | 2.10 | 3.19 | 2.84 | 2.44 | 2.25 | 2.85 | 23.45 | 100.00% |
| 温度 0.3 | 2.48 | 4.96 | 2.10 | 3.23 | 2.82 | 2.44 | 2.29 | 2.87 | 23.19 | 100.00% |
| 温度 0.7 | 2.45 | 4.99 | 2.11 | 3.19 | 2.83 | 2.43 | 2.28 | 2.87 | 23.15 | 100.00% |
| 温度 1.0 | 2.45 | 4.97 | 2.10 | 3.18 | 2.80 | 2.41 | 2.26 | 2.84 | 22.99 | 100.00% |
### 航向控制 - 相对角度

| 配置 | 原地转一圈 |右转180度 |向右转30度 |向左转45度 |左转90度 |逆时针转60度 |顺时针转90度 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|----------|--------|
| 温度 0.0 | 2.80 | 93.25 | 2.91 | 3.15 | 3.17 | 2.41 | 3.18 | 110.87 | 85.71% |
| 温度 0.3 | 2.81 | 93.49 | 2.79 | 3.70 | 3.22 | 2.69 | 3.20 | 111.90 | 85.71% |
| 温度 0.7 | 2.79 | 93.55 | 2.89 | 3.16 | 3.20 | 2.66 | 3.17 | 111.43 | 85.71% |
| 温度 1.0 | 2.83 | 93.30 | 2.91 | 3.40 | 3.22 | 2.69 | 3.20 | 111.56 | 85.71% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... |起飞，向右2m，然后... |起飞，向后2m，然后... |起飞，向左1m，然后... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| 温度 0.0 | 2.26 | 2.33 | 2.00 | 2.50 | 9.09 | 100.00% |
| 温度 0.3 | 2.30 | 2.32 | 1.99 | 2.48 | 9.09 | 100.00% |
| 温度 0.7 | 2.27 | 2.36 | 2.00 | 2.49 | 9.13 | 100.00% |
| 温度 1.0 | 2.33 | 2.32 | 2.02 | 2.51 | 9.17 | 100.00% |
### 组合指令 - 多步骤

| 配置 | 起飞到2米，然后向前... |起飞，升高2m，向前... |起飞，向前3m，向右... | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| 温度 0.0 | 3.26 | 2.02 | 3.43 | 8.72 | 100.00% |
| 温度 0.3 | 3.23 | 2.03 | 3.41 | 8.67 | 100.00% |
| 温度 0.7 | 3.29 | 2.08 | 3.40 | 8.77 | 100.00% |
| 温度 1.0 | 3.23 | 2.04 | 3.42 | 8.69 | 100.00% |
### 组合指令 - 含航向控制

| 配置 | 起飞，向前2m，向左... |起飞，机头朝东，向前... |起飞，转向正南，然后... |起飞，顺时针转180... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| 温度 0.0 | 3.96 | 2.56 | 3.60 | 4.53 | 14.64 | 75.00% |
| 温度 0.3 | 3.92 | 2.56 | 3.60 | 4.50 | 14.59 | 75.00% |
| 温度 0.7 | 3.89 | 2.57 | 3.61 | 4.47 | 14.54 | 75.00% |
| 温度 1.0 | 3.95 | 2.58 | 3.60 | 4.65 | 14.78 | 75.00% |
### 复杂组合

| 配置 | 起飞到3米，机头朝北... |起飞，升高1m，原地... | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| 温度 0.0 | 12.01 | 3.11 | 15.12 | 100.00% |
| 温度 0.3 | 6.88 | 3.09 | 9.97 | 100.00% |
| 温度 0.7 | 6.91 | 3.05 | 9.96 | 100.00% |
| 温度 1.0 | 7.10 | 3.25 | 10.35 | 100.00% |
### 边界情况

| 配置 | 向前0.5m |向右转0度 |起飞到0.5米 | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| 温度 0.0 | 3.00 | 3.04 | 2.46 | 8.49 | 100.00% |
| 温度 0.3 | 3.00 | 3.07 | 2.44 | 8.51 | 100.00% |
| 温度 0.7 | 2.98 | 3.06 | 2.45 | 8.49 | 100.00% |
| 温度 1.0 | 3.03 | 3.09 | 2.48 | 8.60 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |航向控制 - 绝对角度 |航向控制 - 相对角度 |组合指令 - 简单序列 |组合指令 - 多步骤 |组合指令 - 含航向控制 |复杂组合 |边界情况 | 总时间 | 总匹配率 |
|------|------|------|------|------|------|------|------|------|------|----------|--------|
| 温度 0.0 | 10.29 | 19.71 | 23.45 | 110.87 | 9.09 | 8.72 | 14.64 | 15.12 | 8.49 | 220.38 | 95.35% |
| 温度 0.3 | 10.34 | 19.84 | 23.19 | 111.90 | 9.09 | 8.67 | 14.59 | 9.97 | 8.51 | 216.11 | 95.35% |
| 温度 0.7 | 10.24 | 19.25 | 23.15 | 111.43 | 9.13 | 8.77 | 14.54 | 9.96 | 8.49 | 214.95 | 95.35% |
| 温度 1.0 | 10.29 | 19.70 | 22.99 | 111.56 | 9.17 | 8.69 | 14.78 | 10.35 | 8.60 | 216.14 | 95.35% |

## 性能总结

- 温度 0.0: 总时间 = 220.38秒, 匹配率 = 95.35% (41/43)
- 温度 0.3: 总时间 = 216.11秒, 匹配率 = 95.35% (41/43)
- 温度 0.7: 总时间 = 214.95秒, 匹配率 = 95.35% (41/43)
- 温度 1.0: 总时间 = 216.14秒, 匹配率 = 95.35% (41/43)

## 最佳配置分析

**最快配置**: 温度 0.7
**总处理时间**: 214.95秒
**最高准确率配置**: 温度 0.0, 温度 0.3, 温度 0.7, 温度 1.0
**匹配率**: 95.35%

### 温度参数对比分析

- 温度 0.0: 总时间 = 220.38秒, 匹配率 = 95.35% (41/43)
- 温度 0.3: 总时间 = 216.11秒, 匹配率 = 95.35% (41/43)
- 温度 0.7: 总时间 = 214.95秒, 匹配率 = 95.35% (41/43)
- 温度 1.0: 总时间 = 216.14秒, 匹配率 = 95.35% (41/43)

## 测试日志

### === 测试配置: 温度 0.0 ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}}]
\`\`\`
处理时间: 2.65秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 降落
期待输出: [{"action":"land"}]
模型输出: [{"action":"land"}]
处理时间: 1.96秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 2.81秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 2.86秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 5.0}}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 2.78秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
\`\`\`
处理时间: 2.06秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 向左1m
期待输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
处理时间: 2.18秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'

测试指令: 向右5m
期待输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
\`\`\`
处理时间: 2.68秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 5.0}}'

测试指令: 升高2m
期待输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
处理时间: 2.81秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'

测试指令: 降低1m
期待输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
\`\`\`
处理时间: 2.44秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'

测试指令: 向前飞10米
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
\`\`\`
处理时间: 1.94秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 10.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 10.0}}'

测试指令: 往后退3米
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 2.82秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 机头朝北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 4.97秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 机头朝东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
\`\`\`
处理时间: 2.82秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 机头朝南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
\`\`\`
处理时间: 2.10秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 机头朝西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
\`\`\`
处理时间: 3.19秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
\`\`\`
处理时间: 2.44秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.84秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 转向正南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.25秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 转向正西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 2.85秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 3.15秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -45.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -45.0}}'

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 2.91秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 30.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 30.0}}'

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
\`\`\`
处理时间: 3.18秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 2.41秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -60.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -60.0}}'

测试指令: 原地转一圈
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
处理时间: 2.80秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 3.17秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'

测试指令: 右转180度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
模型输出: 
处理时间: 93.25秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.26秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 2.00秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向左1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
\`\`\`
处理时间: 2.50秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向右2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.33秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米，然后向前飞1米，最后降落
期待输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
处理时间: 3.26秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.02秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前3m，向右2m，向后3m，向左2m，降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
处理时间: 3.43秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 2.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 3.60秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前2m，向左转90度，再向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 3.96秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
\`\`\`
处理时间: 2.56秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，顺时针转180度，向前3m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 4.53秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 12.01秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 3.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 3.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.11秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前0.5m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
\`\`\`
处理时间: 3.00秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 0.5}}'

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 2.46秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 0.5}}'

测试指令: 向右转0度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
处理时间: 3.04秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 0.0}}'

============================================================
测试完成！
总测试时间: 220.42秒
匹配率: 95.35% (41/43)
============================================================
总测试时间: 220.42秒
匹配率: 95.35% (41/43)
```

### === 测试配置: 温度 0.3 ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}}]
\`\`\`
处理时间: 2.66秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 降落
期待输出: [{"action":"land"}]
模型输出: [{"action":"land"}]
处理时间: 1.98秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 2.83秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 2.87秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 5.0}}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 2.76秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
\`\`\`
处理时间: 2.04秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 向左1m
期待输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
处理时间: 2.23秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'

测试指令: 向右5m
期待输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
\`\`\`
处理时间: 2.70秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 5.0}}'

测试指令: 升高2m
期待输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
处理时间: 2.82秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'

测试指令: 降低1m
期待输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
\`\`\`
处理时间: 2.46秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'

测试指令: 向前飞10米
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
\`\`\`
处理时间: 1.98秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 10.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 10.0}}'

测试指令: 往后退3米
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 2.86秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 机头朝北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 4.96秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 机头朝东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.48秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 机头朝南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
\`\`\`
处理时间: 2.10秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 机头朝西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
\`\`\`
处理时间: 3.23秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
\`\`\`
处理时间: 2.44秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.82秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 转向正南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.29秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 转向正西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 2.87秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 3.70秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -45.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -45.0}}'

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 2.79秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 30.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 30.0}}'

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
\`\`\`
处理时间: 3.20秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 2.69秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -60.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -60.0}}'

测试指令: 原地转一圈
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
处理时间: 2.81秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 3.22秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'

测试指令: 右转180度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
模型输出: 
处理时间: 93.49秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.30秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 1.99秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向左1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
\`\`\`
处理时间: 2.48秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向右2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.32秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米，然后向前飞1米，最后降落
期待输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
处理时间: 3.23秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.03秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前3m，向右2m，向后3m，向左2m，降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
处理时间: 3.41秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 2.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 3.60秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前2m，向左转90度，再向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 3.92秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
\`\`\`
处理时间: 2.56秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，顺时针转180度，向前3m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 4.50秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 6.88秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 3.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 3.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.09秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前0.5m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
\`\`\`
处理时间: 3.00秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 0.5}}'

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 2.44秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 0.5}}'

测试指令: 向右转0度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
处理时间: 3.07秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 0.0}}'

============================================================
测试完成！
总测试时间: 216.14秒
匹配率: 95.35% (41/43)
============================================================
总测试时间: 216.14秒
匹配率: 95.35% (41/43)
```

### === 测试配置: 温度 0.7 ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}}]
\`\`\`
处理时间: 2.65秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 降落
期待输出: [{"action":"land"}]
模型输出: [{"action":"land"}]
处理时间: 1.96秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 2.79秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 2.83秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 5.0}}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 2.75秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
\`\`\`
处理时间: 2.05秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 向左1m
期待输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
处理时间: 2.22秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'

测试指令: 向右5m
期待输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
\`\`\`
处理时间: 2.69秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 5.0}}'

测试指令: 升高2m
期待输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
处理时间: 2.79秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'

测试指令: 降低1m
期待输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
\`\`\`
处理时间: 2.42秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'

测试指令: 向前飞10米
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
\`\`\`
处理时间: 1.96秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 10.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 10.0}}'

测试指令: 往后退3米
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
\`\`\`
处理时间: 2.37秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 机头朝北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 4.99秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 机头朝东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.45秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 机头朝南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
\`\`\`
处理时间: 2.11秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 机头朝西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
\`\`\`
处理时间: 3.19秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
\`\`\`
处理时间: 2.43秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.83秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 转向正南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.28秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 转向正西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 2.87秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 3.16秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -45.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -45.0}}'

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 2.89秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 30.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 30.0}}'

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
\`\`\`
处理时间: 3.17秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 2.66秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -60.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -60.0}}'

测试指令: 原地转一圈
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
处理时间: 2.79秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 3.20秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'

测试指令: 右转180度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
模型输出: 
处理时间: 93.55秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.27秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 2.00秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向左1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
\`\`\`
处理时间: 2.49秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向右2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.36秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米，然后向前飞1米，最后降落
期待输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
处理时间: 3.29秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.08秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前3m，向右2m，向后3m，向左2m，降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
处理时间: 3.40秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 2.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 3.61秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前2m，向左转90度，再向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 3.89秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
\`\`\`
处理时间: 2.57秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，顺时针转180度，向前3m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 4.47秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 6.91秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 3.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 3.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.05秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前0.5m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
\`\`\`
处理时间: 2.98秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 0.5}}'

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 2.45秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 0.5}}'

测试指令: 向右转0度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
处理时间: 3.06秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 0.0}}'

============================================================
测试完成！
总测试时间: 214.98秒
匹配率: 95.35% (41/43)
============================================================
总测试时间: 214.98秒
匹配率: 95.35% (41/43)
```

### === 测试配置: 温度 1.0 ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}}]
\`\`\`
处理时间: 2.67秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 降落
期待输出: [{"action":"land"}]
模型输出: [{"action":"land"}]
处理时间: 1.95秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 2.81秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 2.85秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 5.0}}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 2.74秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
\`\`\`
处理时间: 2.04秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 向左1m
期待输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
处理时间: 2.23秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'

测试指令: 向右5m
期待输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
\`\`\`
处理时间: 2.70秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 5.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 5.0}}'

测试指令: 升高2m
期待输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"up","distance":2.0}}]
处理时间: 2.80秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'

测试指令: 降低1m
期待输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
\`\`\`
处理时间: 2.47秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'

测试指令: 向前飞10米
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
\`\`\`
处理时间: 1.94秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 10.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 10.0}}'

测试指令: 往后退3米
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 2.79秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'

测试指令: 机头朝北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 4.97秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 机头朝东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.45秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 机头朝南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
\`\`\`
处理时间: 2.10秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 机头朝西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
\`\`\`
处理时间: 3.18秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
\`\`\`
处理时间: 2.41秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.80秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 转向正南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.26秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 转向正西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 2.84秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 270.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 270.0}}'

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 3.40秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -45.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -45.0}}'

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 2.91秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 30.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 30.0}}'

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
\`\`\`
处理时间: 3.20秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 2.69秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -60.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -60.0}}'

测试指令: 原地转一圈
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
处理时间: 2.83秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 3.22秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'

测试指令: 右转180度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
模型输出: 
处理时间: 93.30秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.33秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 2.02秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向左1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
\`\`\`
处理时间: 2.51秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向右2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.32秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到2米，然后向前飞1米，最后降落
期待输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
处理时间: 3.23秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 2.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.04秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前3m，向右2m，向后3m，向左2m，降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"direction_move","params":{"orientation":"backward","distance":3.0}},{"action":"direction_move","params":{"orientation":"left","distance":2.0}},{"action":"land"}]
处理时间: 3.42秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "right",
      "distance": 2.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "backward",
      "distance": 3.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "left",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "left", "distance": 2.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 3.60秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，向前2m，向左转90度，再向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 3.95秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": -90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 2.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
\`\`\`
处理时间: 2.58秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，顺时针转180度，向前3m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 4.65秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 7.10秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 3.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_to",
      "angle": 0.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 90.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 5.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 3.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 0.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 4: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 90.0}}'
步骤 5: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 5.0}}'
步骤 6: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.25秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "up",
      "distance": 1.0
    }
  },
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 360.0
    }
  },
  {
    "action": "direction_move",
    "params": {
      "orientation": "down",
      "distance": 1.0
    }
  },
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "up", "distance": 1.0}}'
步骤 3: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 360.0}}'
步骤 4: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "down", "distance": 1.0}}'
步骤 5: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前0.5m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
模型输出: \`\`\`json
[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
\`\`\`
处理时间: 3.03秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 0.5}}'

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 2.48秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 0.5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 0.5}}'

测试指令: 向右转0度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
处理时间: 3.09秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 0.0}}'

============================================================
测试完成！
总测试时间: 216.17秒
匹配率: 95.35% (41/43)
============================================================
总测试时间: 216.17秒
匹配率: 95.35% (41/43)
```

