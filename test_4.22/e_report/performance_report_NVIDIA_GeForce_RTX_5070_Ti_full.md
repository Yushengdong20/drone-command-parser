# 无人机指令解析器性能测试报告

## 测试配置

### qwen3.5:latest
- 模型: qwen3.5:latest
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500
}

### qwen3.5:0.8b
- 模型: qwen3.5:0.8b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500
}

### qwen3.5:2b
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500
}

### qwen3.5:4b
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 16384,
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500
}

## 性能数据

### 基础动作 - 起飞降落

| 模型 | 起飞 |起飞到2米 |起飞到5米 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 7.60 | 6.11 | 5.10 | 5.26 | 24.06 | 100.00% |
| qwen3.5:0.8b | 2.97 | 1.60 | 2.00 | 1.55 | 8.13 | 50.00% |
| qwen3.5:2b | 4.99 | 2.82 | 2.89 | 1.98 | 12.69 | 100.00% |
| qwen3.5:4b | 11.68 | 9.68 | 12.98 | 3.92 | 38.26 | 100.00% |
### 基础动作 - 方向移动

| 模型 | 升高2m |向前2m |向前飞10米 |向右5m |向后3m |向左1m |往后退3米 |降低1m | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 10.66 | 5.02 | 5.18 | 12.10 | 5.54 | 7.79 | 6.81 | 9.84 | 62.94 | 100.00% |
| qwen3.5:0.8b | 1.38 | 1.42 | 1.31 | 2.33 | 1.56 | 2.31 | 1.76 | 1.16 | 13.22 | 75.00% |
| qwen3.5:2b | 2.90 | 2.79 | 1.97 | 2.72 | 2.07 | 2.20 | 2.87 | 2.43 | 19.96 | 100.00% |
| qwen3.5:4b | 16.54 | 9.05 | 9.53 | 10.37 | 5.61 | 15.79 | 9.39 | 10.49 | 86.78 | 100.00% |
### 航向控制 - 绝对角度

| 模型 | 机头朝东 |机头朝北 |机头朝南 |机头朝西 |转向正东 |转向正北 |转向正南 |转向正西 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 11.66 | 19.51 | 11.82 | 12.62 | 7.91 | 10.31 | 13.07 | 17.51 | 104.43 | 100.00% |
| qwen3.5:0.8b | 1.80 | 3.46 | 2.19 | 758.04 | 1.48 | 2.48 | 1.58 | 2.13 | 773.17 | 62.50% |
| qwen3.5:2b | 2.45 | 5.03 | 2.12 | 3.19 | 2.83 | 2.41 | 2.28 | 2.88 | 23.18 | 100.00% |
| qwen3.5:4b | 12.35 | 22.73 | 19.00 | 14.60 | 24.91 | 14.65 | 6.31 | 8.44 | 122.99 | 100.00% |
### 航向控制 - 相对角度

| 模型 | 原地转一圈 |右转180度 |向右转30度 |向左转45度 |左转90度 |逆时针转60度 |顺时针转90度 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 16.22 | 7.19 | 11.15 | 6.85 | 10.07 | 15.53 | 7.30 | 74.32 | 100.00% |
| qwen3.5:0.8b | 1.86 | 1.87 | 71.84 | 1.72 | 3.02 | 2.43 | 70.91 | 153.66 | 57.14% |
| qwen3.5:2b | 2.81 | 95.12 | 2.91 | 3.18 | 3.24 | 2.66 | 3.20 | 113.12 | 85.71% |
| qwen3.5:4b | 34.06 | 6.00 | 15.62 | 30.87 | 9.17 | 11.29 | 16.32 | 123.32 | 100.00% |
### 组合指令 - 简单序列

| 模型 | 起飞，向前2m，然后... |起飞，向右2m，然后... |起飞，向后2m，然后... |起飞，向左1m，然后... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 16.05 | 12.67 | 12.03 | 13.25 | 53.99 | 100.00% |
| qwen3.5:0.8b | 1.69 | 2.19 | 1.57 | 2.48 | 7.94 | 100.00% |
| qwen3.5:2b | 2.29 | 2.37 | 2.03 | 2.55 | 9.23 | 100.00% |
| qwen3.5:4b | 24.87 | 11.93 | 23.46 | 15.81 | 76.07 | 100.00% |
### 组合指令 - 多步骤

| 模型 | 起飞到2米，然后向前... |起飞，升高2m，向前... |起飞，向前3m，向右... | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| qwen3.5:latest | 7.28 | 22.18 | 21.41 | 50.87 | 100.00% |
| qwen3.5:0.8b | 2.29 | 1.81 | 761.62 | 765.72 | 66.67% |
| qwen3.5:2b | 3.30 | 2.02 | 3.42 | 8.74 | 100.00% |
| qwen3.5:4b | 10.41 | 10.01 | 13.81 | 34.23 | 100.00% |
### 组合指令 - 含航向控制

| 模型 | 起飞，向前2m，向左... |起飞，机头朝东，向前... |起飞，转向正南，然后... |起飞，顺时针转180... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 31.91 | 8.29 | 35.38 | 13.10 | 88.68 | 100.00% |
| qwen3.5:0.8b | 2.97 | 2.31 | 2.74 | 2.97 | 10.99 | 75.00% |
| qwen3.5:2b | 4.01 | 2.61 | 3.63 | 4.56 | 14.81 | 75.00% |
| qwen3.5:4b | 16.31 | 10.80 | 17.57 | 16.00 | 60.68 | 100.00% |
### 复杂组合

| 模型 | 起飞到3米，机头朝北... |起飞，升高1m，原地... | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| qwen3.5:latest | 15.47 | 40.57 | 56.04 | 100.00% |
| qwen3.5:0.8b | 71.06 | 3.70 | 74.76 | 50.00% |
| qwen3.5:2b | 6.96 | 3.11 | 10.07 | 100.00% |
| qwen3.5:4b | 18.95 | 15.02 | 33.97 | 100.00% |
### 边界情况

| 模型 | 向前0.5m |向右转0度 |起飞到0.5米 | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| qwen3.5:latest | 5.35 | 21.31 | 7.06 | 33.72 | 100.00% |
| qwen3.5:0.8b | 6.97 | 71.38 | 1.63 | 79.97 | 33.33% |
| qwen3.5:2b | 3.08 | 3.07 | 2.48 | 8.63 | 100.00% |
| qwen3.5:4b | 9.52 | 20.43 | 13.54 | 43.49 | 100.00% |

### 汇总

| 模型 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |航向控制 - 绝对角度 |航向控制 - 相对角度 |组合指令 - 简单序列 |组合指令 - 多步骤 |组合指令 - 含航向控制 |复杂组合 |边界情况 | 总时间 | 总匹配率 |
|------|------|------|------|------|------|------|------|------|------|----------|--------|
| qwen3.5:latest | 24.06 | 62.94 | 104.43 | 74.32 | 53.99 | 50.87 | 88.68 | 56.04 | 33.72 | 549.06 | 100.00% |
| qwen3.5:0.8b | 8.13 | 13.22 | 773.17 | 153.66 | 7.94 | 765.72 | 10.99 | 74.76 | 79.97 | 1887.55 | 65.12% |
| qwen3.5:2b | 12.69 | 19.96 | 23.18 | 113.12 | 9.23 | 8.74 | 14.81 | 10.07 | 8.63 | 220.42 | 95.35% |
| qwen3.5:4b | 38.26 | 86.78 | 122.99 | 123.32 | 76.07 | 34.23 | 60.68 | 33.97 | 43.49 | 619.80 | 100.00% |

## 性能总结

- qwen3.5:latest: 总时间 = 549.06秒, 匹配率 = 100.00% (43/43)
- qwen3.5:0.8b: 总时间 = 1887.55秒, 匹配率 = 65.12% (28/43)
- qwen3.5:2b: 总时间 = 220.42秒, 匹配率 = 95.35% (41/43)
- qwen3.5:4b: 总时间 = 619.80秒, 匹配率 = 100.00% (43/43)

## 最佳配置分析

**最快配置**: qwen3.5:2b
**总处理时间**: 220.42秒
**最高准确率配置**: qwen3.5:latest, qwen3.5:4b
**匹配率**: 100.00%

### 模型对比分析

- qwen3.5:latest: 总时间 = 549.06秒, 匹配率 = 100.00% (43/43)
- qwen3.5:0.8b: 总时间 = 1887.55秒, 匹配率 = 65.12% (28/43)
- qwen3.5:2b: 总时间 = 220.42秒, 匹配率 = 95.35% (41/43)
- qwen3.5:4b: 总时间 = 619.80秒, 匹配率 = 100.00% (43/43)

## 测试日志

### === 测试配置: qwen3.5:latest ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 7.60秒
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
处理时间: 5.26秒
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
处理时间: 6.11秒
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
处理时间: 5.10秒
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
处理时间: 5.02秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 5.54秒
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
处理时间: 7.79秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
处理时间: 12.10秒
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
处理时间: 10.66秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
处理时间: 9.84秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
处理时间: 5.18秒
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
处理时间: 6.81秒
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
处理时间: 19.51秒
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
处理时间: 11.66秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 11.82秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 12.62秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 10.31秒
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
处理时间: 7.91秒
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
处理时间: 13.07秒
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
处理时间: 17.51秒
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
处理时间: 6.85秒
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
处理时间: 11.15秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
处理时间: 7.30秒
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
处理时间: 15.53秒
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
处理时间: 16.22秒
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
处理时间: 10.07秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
处理时间: 7.19秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 180.0}}'

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 16.05秒
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
处理时间: 12.03秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
处理时间: 13.25秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
处理时间: 12.67秒
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
处理时间: 7.28秒
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
处理时间: 22.18秒
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
处理时间: 21.41秒
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
处理时间: 35.38秒
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
处理时间: 31.91秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 8.29秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 13.10秒
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
      "mode": "turn_by",
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
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 15.47秒
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
处理时间: 40.57秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
处理时间: 5.35秒
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
处理时间: 7.06秒
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
处理时间: 21.31秒
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
总测试时间: 549.09秒
匹配率: 100.00% (43/43)
============================================================
总测试时间: 549.09秒
匹配率: 100.00% (43/43)
```

### === 测试配置: qwen3.5:0.8b ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 2.97秒
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
模型输出: [{"action":"land","params":{}}]
处理时间: 1.55秒
处理后的指令:
[
  {
    "action": "land",
    "params": {}
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land", "params": {}}'

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 1.60秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 2.00秒
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
处理时间: 1.42秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":3.0}}]
处理时间: 1.56秒
处理后的指令:
[
  {
    "action": "direction_move",
    "params": {
      "orientation": "forward",
      "distance": 3.0
    }
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'

测试指令: 向左1m
期待输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"left","distance":1.0}}]
处理时间: 2.31秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
处理时间: 2.33秒
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
处理时间: 1.38秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 1.16秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 1.0
    }
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'

测试指令: 向前飞10米
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
处理时间: 1.31秒
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
处理时间: 1.76秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 3.46秒
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
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}}'

测试指令: 机头朝东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 1.80秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.19秒
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
模型输出: 
处理时间: 758.04秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 2.48秒
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
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 1.48秒
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
处理时间: 1.58秒
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
处理时间: 2.13秒
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
处理时间: 1.72秒
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
模型输出: 
处理时间: 71.84秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: 
处理时间: 70.91秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 2.43秒
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
处理时间: 1.86秒
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
处理时间: 3.02秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 1.87秒
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
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 1.69秒
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
处理时间: 1.57秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
处理时间: 2.19秒
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
处理时间: 2.29秒
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
处理时间: 1.81秒
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
模型输出: 
处理时间: 761.62秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 2.74秒
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
处理时间: 2.97秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.31秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},"action":"direction_move","params":{"orientation":"forward","distance":3.0},"action":"land"}]
处理时间: 2.97秒
错误: 解析指令失败
详情: Expecting ',' delimiter: line 1 column 56 (char 55)

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: 
处理时间: 71.06秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.70秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 6.97秒
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
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}}'
步骤 3: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 1.63秒
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
模型输出: 
处理时间: 71.38秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

============================================================
测试完成！
总测试时间: 1887.58秒
匹配率: 65.12% (28/43)
============================================================
总测试时间: 1887.58秒
匹配率: 65.12% (28/43)
```

### === 测试配置: qwen3.5:2b ===

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
处理时间: 4.99秒
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
处理时间: 2.82秒
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
处理时间: 2.89秒
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
处理时间: 2.79秒
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
处理时间: 2.07秒
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
处理时间: 2.20秒
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
处理时间: 2.72秒
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
处理时间: 2.90秒
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
处理时间: 2.43秒
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
处理时间: 1.97秒
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
处理时间: 2.87秒
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
处理时间: 5.03秒
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
处理时间: 2.12秒
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
处理时间: 2.88秒
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
处理时间: 3.18秒
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
处理时间: 3.24秒
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
处理时间: 95.12秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.29秒
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
处理时间: 2.55秒
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
处理时间: 2.37秒
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
处理时间: 3.30秒
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
处理时间: 3.63秒
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
处理时间: 4.01秒
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
处理时间: 2.61秒
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
处理时间: 4.56秒
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
处理时间: 6.96秒
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
处理时间: 3.08秒
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
总测试时间: 220.45秒
匹配率: 95.35% (41/43)
============================================================
总测试时间: 220.45秒
匹配率: 95.35% (41/43)
```

### === 测试配置: qwen3.5:4b ===

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 11.68秒
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
处理时间: 3.92秒
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
处理时间: 9.68秒
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
模型输出: [{"action":"take_off","params":{"height":5}}]
处理时间: 12.98秒
处理后的指令:
[
  {
    "action": "take_off",
    "params": {
      "height": 5
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 5}}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 9.05秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 5.61秒
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
处理时间: 15.79秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
处理时间: 10.37秒
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
处理时间: 16.54秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
处理时间: 10.49秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":10.0}}]
处理时间: 9.53秒
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
处理时间: 9.39秒
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
处理时间: 22.73秒
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
处理时间: 12.35秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 19.00秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 14.60秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 14.65秒
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
处理时间: 24.91秒
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
处理时间: 6.31秒
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
处理时间: 8.44秒
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
处理时间: 30.87秒
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
处理时间: 15.62秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
处理时间: 16.32秒
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
处理时间: 11.29秒
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
处理时间: 34.06秒
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
处理时间: 9.17秒
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
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
处理时间: 6.00秒
处理后的指令:
[
  {
    "action": "yaw_change",
    "params": {
      "mode": "turn_by",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 180.0}}'

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 24.87秒
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
处理时间: 23.46秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"left","distance":1.0}},{"action":"land"}]
处理时间: 15.81秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
处理时间: 11.93秒
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
处理时间: 10.41秒
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
处理时间: 10.01秒
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
处理时间: 13.81秒
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
处理时间: 17.57秒
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
处理时间: 16.31秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 10.80秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
处理时间: 16.00秒
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
      "mode": "turn_by",
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
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "take_off", "params": {"height": 1.0}}'
步骤 2: redis-cli set drone_command '{"action": "yaw_change", "params": {"mode": "turn_by", "angle": 180.0}}'
步骤 3: redis-cli set drone_command '{"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}'
步骤 4: redis-cli set drone_command '{"action": "land"}'

测试指令: 起飞到3米，机头朝北，向前5m，向右转90度，向前5m，降落
期待输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":3.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 18.95秒
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
处理时间: 15.02秒
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
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
处理时间: 9.52秒
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
处理时间: 13.54秒
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
处理时间: 20.43秒
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
总测试时间: 619.83秒
匹配率: 100.00% (43/43)
============================================================
总测试时间: 619.83秒
匹配率: 100.00% (43/43)
```

