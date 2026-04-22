# 无人机指令解析器top_p参数测试报告

## 测试配置

### top_p 0.1
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 2048,
  "temperature": 0.3,
  "max_new_tokens": 500,
  "top_p": 0.1
}

### top_p 0.3
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 2048,
  "temperature": 0.3,
  "max_new_tokens": 500,
  "top_p": 0.3
}

### top_p 0.5
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 2048,
  "temperature": 0.3,
  "max_new_tokens": 500,
  "top_p": 0.5
}

### top_p 0.7
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 2048,
  "temperature": 0.3,
  "max_new_tokens": 500,
  "top_p": 0.7
}

### top_p 1.0
- 模型: qwen3.5:4b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "num_ctx": 2048,
  "temperature": 0.3,
  "max_new_tokens": 500,
  "top_p": 1.0
}

## 性能数据

### 基础动作 - 起飞降落

| 配置 | 起飞 |起飞到2米 |起飞到5米 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| top_p 0.1 | 11.54 | 9.82 | 13.46 | 3.88 | 38.70 | 100.00% |
| top_p 0.3 | 9.24 | 11.26 | 60.93 | 3.99 | 85.42 | 75.00% |
| top_p 0.5 | 9.40 | 8.29 | 14.56 | 6.92 | 39.17 | 100.00% |
| top_p 0.7 | 4.84 | 7.39 | 25.45 | 11.92 | 49.60 | 100.00% |
| top_p 1.0 | 8.69 | 8.92 | 8.02 | 3.51 | 29.15 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 升高2m |向前2m |向前飞10米 |向右5m |向后3m |向左1m |往后退3米 |降低1m | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| top_p 0.1 | 13.03 | 9.15 | 9.61 | 10.44 | 5.73 | 17.13 | 9.37 | 10.87 | 85.32 | 100.00% |
| top_p 0.3 | 13.01 | 9.06 | 9.67 | 10.35 | 5.67 | 17.06 | 9.45 | 10.90 | 85.18 | 100.00% |
| top_p 0.5 | 9.18 | 12.44 | 9.20 | 7.91 | 19.31 | 12.35 | 9.11 | 11.46 | 90.95 | 100.00% |
| top_p 0.7 | 35.89 | 5.22 | 9.28 | 13.11 | 46.26 | 70.39 | 7.86 | 8.05 | 196.05 | 75.00% |
| top_p 1.0 | 15.94 | 20.61 | 5.56 | 24.07 | 14.89 | 8.13 | 8.93 | 13.84 | 111.97 | 100.00% |
### 航向控制 - 绝对角度

| 配置 | 机头朝东 |机头朝北 |机头朝南 |机头朝西 |转向正东 |转向正北 |转向正南 |转向正西 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|------|----------|--------|
| top_p 0.1 | 16.70 | 14.18 | 12.78 | 11.16 | 10.20 | 18.46 | 6.45 | 8.65 | 98.58 | 100.00% |
| top_p 0.3 | 16.99 | 16.22 | 12.98 | 12.26 | 10.44 | 19.14 | 6.45 | 8.87 | 103.35 | 100.00% |
| top_p 0.5 | 40.82 | 27.61 | 63.74 | 15.40 | 12.39 | 36.35 | 6.97 | 9.47 | 212.74 | 75.00% |
| top_p 0.7 | 26.07 | 10.55 | 9.95 | 20.66 | 6.00 | 15.96 | 10.89 | 37.20 | 137.28 | 87.50% |
| top_p 1.0 | 18.66 | 16.31 | 15.12 | 35.61 | 10.04 | 11.03 | 15.89 | 27.66 | 150.34 | 75.00% |
### 航向控制 - 相对角度

| 配置 | 原地转一圈 |右转180度 |向右转30度 |向左转45度 |左转90度 |逆时针转60度 |顺时针转90度 | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|------|------|------|----------|--------|
| top_p 0.1 | 45.09 | 86.73 | 11.62 | 64.71 | 9.49 | 11.19 | 11.37 | 240.21 | 57.14% |
| top_p 0.3 | 36.55 | 172.99 | 11.84 | 27.13 | 9.17 | 11.18 | 27.26 | 296.12 | 42.86% |
| top_p 0.5 | 30.58 | 9.93 | 9.44 | 17.20 | 36.43 | 10.97 | 14.83 | 129.37 | 71.43% |
| top_p 0.7 | 22.07 | 35.58 | 10.28 | 14.62 | 10.10 | 173.73 | 5.42 | 271.80 | 71.43% |
| top_p 1.0 | 24.89 | 10.62 | 9.15 | 11.89 | 66.08 | 13.77 | 6.00 | 142.40 | 100.00% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... |起飞，向右2m，然后... |起飞，向后2m，然后... |起飞，向左1m，然后... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| top_p 0.1 | 28.89 | 11.71 | 18.62 | 18.73 | 77.95 | 100.00% |
| top_p 0.3 | 29.04 | 11.56 | 11.59 | 22.19 | 74.38 | 100.00% |
| top_p 0.5 | 46.56 | 24.02 | 13.65 | 11.30 | 95.53 | 100.00% |
| top_p 0.7 | 10.65 | 13.08 | 23.85 | 9.47 | 57.05 | 100.00% |
| top_p 1.0 | 34.83 | 22.95 | 7.28 | 16.43 | 81.49 | 75.00% |
### 组合指令 - 多步骤

| 配置 | 起飞到2米，然后向前... |起飞，升高2m，向前... |起飞，向前3m，向右... | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| top_p 0.1 | 11.10 | 10.78 | 9.93 | 31.82 | 66.67% |
| top_p 0.3 | 10.83 | 10.78 | 9.92 | 31.53 | 66.67% |
| top_p 0.5 | 28.21 | 18.85 | 173.44 | 220.49 | 33.33% |
| top_p 0.7 | 11.71 | 15.77 | 19.72 | 47.20 | 100.00% |
| top_p 1.0 | 45.16 | 12.22 | 19.50 | 76.89 | 66.67% |
### 组合指令 - 含航向控制

| 配置 | 起飞，向前2m，向左... |起飞，机头朝东，向前... |起飞，转向正南，然后... |起飞，顺时针转180... | 分类总时间 | 分类匹配率 |
|------|------|------|------|------|----------|--------|
| top_p 0.1 | 18.78 | 22.72 | 10.56 | 14.48 | 66.54 | 100.00% |
| top_p 0.3 | 12.57 | 14.64 | 10.65 | 14.32 | 52.18 | 100.00% |
| top_p 0.5 | 9.91 | 12.25 | 40.45 | 19.14 | 81.75 | 75.00% |
| top_p 0.7 | 59.66 | 19.84 | 22.28 | 11.30 | 113.08 | 75.00% |
| top_p 1.0 | 14.54 | 19.93 | 18.88 | 15.56 | 68.91 | 100.00% |
### 复杂组合

| 配置 | 起飞到3米，机头朝北... |起飞，升高1m，原地... | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| top_p 0.1 | 21.13 | 10.82 | 31.95 | 100.00% |
| top_p 0.3 | 21.36 | 10.96 | 32.32 | 100.00% |
| top_p 0.5 | 36.81 | 18.12 | 54.93 | 50.00% |
| top_p 0.7 | 9.73 | 28.86 | 38.59 | 50.00% |
| top_p 1.0 | 15.53 | 46.92 | 62.45 | 50.00% |
### 边界情况

| 配置 | 向前0.5m |向右转0度 |起飞到0.5米 | 分类总时间 | 分类匹配率 |
|------|------|------|------|----------|--------|
| top_p 0.1 | 108.95 | 23.78 | 10.40 | 143.14 | 66.67% |
| top_p 0.3 | 10.07 | 26.24 | 10.45 | 46.76 | 100.00% |
| top_p 0.5 | 50.46 | 15.53 | 17.38 | 83.37 | 66.67% |
| top_p 0.7 | 28.20 | 12.84 | 10.53 | 51.58 | 100.00% |
| top_p 1.0 | 6.81 | 20.21 | 11.85 | 38.88 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |航向控制 - 绝对角度 |航向控制 - 相对角度 |组合指令 - 简单序列 |组合指令 - 多步骤 |组合指令 - 含航向控制 |复杂组合 |边界情况 | 总时间 | 总匹配率 |
|------|------|------|------|------|------|------|------|------|------|----------|--------|
| top_p 0.1 | 38.70 | 85.32 | 98.58 | 240.21 | 77.95 | 31.82 | 66.54 | 31.95 | 143.14 | 814.19 | 88.37% |
| top_p 0.3 | 85.42 | 85.18 | 103.35 | 296.12 | 74.38 | 31.53 | 52.18 | 32.32 | 46.76 | 807.24 | 86.05% |
| top_p 0.5 | 39.17 | 90.95 | 212.74 | 129.37 | 95.53 | 220.49 | 81.75 | 54.93 | 83.37 | 1008.30 | 79.07% |
| top_p 0.7 | 49.60 | 196.05 | 137.28 | 271.80 | 57.05 | 47.20 | 113.08 | 38.59 | 51.58 | 962.23 | 83.72% |
| top_p 1.0 | 29.15 | 111.97 | 150.34 | 142.40 | 81.49 | 76.89 | 68.91 | 62.45 | 38.88 | 762.46 | 88.37% |

## 性能总结

- top_p 0.1: 总时间 = 814.19秒, 匹配率 = 88.37% (38/43)
- top_p 0.3: 总时间 = 807.24秒, 匹配率 = 86.05% (37/43)
- top_p 0.5: 总时间 = 1008.30秒, 匹配率 = 79.07% (34/43)
- top_p 0.7: 总时间 = 962.23秒, 匹配率 = 83.72% (36/43)
- top_p 1.0: 总时间 = 762.46秒, 匹配率 = 88.37% (38/43)

## 最佳配置分析

**最快配置**: top_p 1.0
**总处理时间**: 762.46秒
**最高准确率配置**: top_p 0.1, top_p 1.0
**匹配率**: 88.37%

### top_p参数对比分析

- top_p 0.1: 总时间 = 814.19秒, 匹配率 = 88.37% (38/43)
- top_p 0.3: 总时间 = 807.24秒, 匹配率 = 86.05% (37/43)
- top_p 0.5: 总时间 = 1008.30秒, 匹配率 = 79.07% (34/43)
- top_p 0.7: 总时间 = 962.23秒, 匹配率 = 83.72% (36/43)
- top_p 1.0: 总时间 = 762.46秒, 匹配率 = 88.37% (38/43)

## 测试日志

### top_p 0.1

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 11.54秒
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
处理时间: 3.88秒
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
处理时间: 9.82秒
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
处理时间: 13.46秒
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
处理时间: 9.15秒
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
处理时间: 5.73秒
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
处理时间: 17.13秒
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
处理时间: 10.44秒
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
处理时间: 13.03秒
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
处理时间: 10.87秒
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
处理时间: 9.61秒
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
处理时间: 9.37秒
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
处理时间: 14.18秒
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
处理时间: 16.70秒
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
处理时间: 12.78秒
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
处理时间: 11.16秒
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
处理时间: 18.46秒
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
处理时间: 10.20秒
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
处理时间: 6.45秒
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
处理时间: 8.65秒
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
模型输出: 
处理时间: 64.71秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 11.62秒
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
处理时间: 11.37秒
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
处理时间: 11.19秒
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
模型输出: 
处理时间: 45.09秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 9.49秒
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
处理时间: 86.73秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 28.89秒
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
处理时间: 18.62秒
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
处理时间: 18.73秒
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
处理时间: 11.71秒
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
处理时间: 11.10秒
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
处理时间: 10.78秒
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
处理时间: 9.93秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 10.56秒
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
模型输出: [
  {"action": "take_off", "params": {"height": 1.0}},
  {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
  {"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}},
  {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
  {"action": "land"}
]
处理时间: 18.78秒
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
处理时间: 22.72秒
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
处理时间: 14.48秒
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
模型输出: [
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
处理时间: 21.13秒
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
处理时间: 10.82秒
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
模型输出: 
处理时间: 108.95秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 10.40秒
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
处理时间: 23.78秒
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
总测试时间: 814.23秒
匹配率: 88.37% (38/43)
============================================================
总测试时间: 814.23秒
匹配率: 88.37% (38/43)
```

### top_p 0.3

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 9.24秒
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
处理时间: 3.99秒
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
处理时间: 11.26秒
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
模型输出: 
处理时间: 60.93秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 9.06秒
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
处理时间: 5.67秒
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
处理时间: 17.06秒
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
处理时间: 10.35秒
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
处理时间: 13.01秒
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
处理时间: 10.90秒
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
处理时间: 9.67秒
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
处理时间: 9.45秒
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
处理时间: 16.22秒
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
处理时间: 16.99秒
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
处理时间: 12.98秒
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
处理时间: 12.26秒
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
处理时间: 19.14秒
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
处理时间: 10.44秒
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
处理时间: 6.45秒
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
处理时间: 8.87秒
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
模型输出: 
处理时间: 27.13秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向右转30度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":30.0}}]
处理时间: 11.84秒
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
模型输出: 
处理时间: 27.26秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 11.18秒
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
模型输出: 
处理时间: 36.55秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

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
模型输出: 
处理时间: 172.99秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 29.04秒
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
处理时间: 11.59秒
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
处理时间: 22.19秒
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
处理时间: 11.56秒
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
处理时间: 10.83秒
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
处理时间: 10.78秒
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
处理时间: 9.92秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 10.65秒
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
模型输出: [
  {"action": "take_off", "params": {"height": 1.0}},
  {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
  {"action": "yaw_change", "params": {"mode": "turn_by", "angle": -90.0}},
  {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
  {"action": "land"}
]
处理时间: 12.57秒
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
处理时间: 14.64秒
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
处理时间: 14.32秒
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
模型输出: [
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
处理时间: 21.36秒
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
处理时间: 10.96秒
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
处理时间: 10.07秒
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
处理时间: 10.45秒
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
处理时间: 26.24秒
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
总测试时间: 807.27秒
匹配率: 86.05% (37/43)
============================================================
总测试时间: 807.27秒
匹配率: 86.05% (37/43)
```

### top_p 0.5

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 9.40秒
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
处理时间: 6.92秒
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
处理时间: 8.29秒
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
处理时间: 14.56秒
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
处理时间: 12.44秒
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
处理时间: 19.31秒
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
处理时间: 12.35秒
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
处理时间: 7.91秒
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
处理时间: 9.18秒
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
处理时间: 11.46秒
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
处理时间: 9.20秒
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
处理时间: 9.11秒
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
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
\`\`\`
处理时间: 27.61秒
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
模型输出: 
处理时间: 40.82秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 机头朝南
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 63.74秒
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
处理时间: 15.40秒
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
模型输出: 
处理时间: 36.35秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 12.39秒
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
处理时间: 6.97秒
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
处理时间: 9.47秒
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
处理时间: 17.20秒
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
处理时间: 9.44秒
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
处理时间: 14.83秒
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
处理时间: 10.97秒
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
模型输出: 
处理时间: 30.58秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 左转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
模型输出: 
处理时间: 36.43秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 右转180度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}}]
处理时间: 9.93秒
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
处理时间: 46.56秒
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
处理时间: 13.65秒
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
处理时间: 11.30秒
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
处理时间: 24.02秒
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
模型输出: 
处理时间: 28.21秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 18.85秒
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
处理时间: 173.44秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，转向正南，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}},{"action":"land"}]
处理时间: 40.45秒
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
模型输出: 
处理时间: 9.91秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 12.25秒
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
处理时间: 19.14秒
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
模型输出: 
处理时间: 36.81秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 18.12秒
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
模型输出: 
处理时间: 50.46秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞到0.5米
期待输出: [{"action":"take_off","params":{"height":0.5}}]
模型输出: [{"action":"take_off","params":{"height":0.5}}]
处理时间: 17.38秒
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
处理时间: 15.53秒
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
总测试时间: 1008.32秒
匹配率: 79.07% (34/43)
============================================================
总测试时间: 1008.32秒
匹配率: 79.07% (34/43)
```

### top_p 0.7

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 4.84秒
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
处理时间: 11.92秒
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
处理时间: 7.39秒
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
处理时间: 25.45秒
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
处理时间: 5.22秒
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
处理时间: 46.26秒
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
模型输出: 
处理时间: 70.39秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向右5m
期待输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"right","distance":5.0}}]
处理时间: 13.11秒
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
模型输出: 
处理时间: 35.89秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 降低1m
期待输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"down","distance":1.0}}]
处理时间: 8.05秒
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
处理时间: 9.28秒
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
处理时间: 7.86秒
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
处理时间: 10.55秒
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
处理时间: 26.07秒
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
处理时间: 9.95秒
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
处理时间: 20.66秒
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
处理时间: 15.96秒
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
处理时间: 6.00秒
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
处理时间: 10.89秒
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
模型输出: 
处理时间: 37.20秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 14.62秒
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
处理时间: 10.28秒
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
处理时间: 5.42秒
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
模型输出: 
处理时间: 173.73秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 原地转一圈
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}}]
处理时间: 22.07秒
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
处理时间: 10.10秒
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
处理时间: 35.58秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 10.65秒
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
处理时间: 23.85秒
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
处理时间: 9.47秒
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
处理时间: 13.08秒
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
处理时间: 11.71秒
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
处理时间: 15.77秒
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
处理时间: 19.72秒
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
处理时间: 22.28秒
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
模型输出: 
处理时间: 59.66秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 19.84秒
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
处理时间: 11.30秒
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
模型输出: 
处理时间: 9.73秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 28.86秒
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
处理时间: 28.20秒
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
处理时间: 10.53秒
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
处理时间: 12.84秒
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
总测试时间: 962.25秒
匹配率: 83.72% (36/43)
============================================================
总测试时间: 962.25秒
匹配率: 83.72% (36/43)
```

### top_p 1.0

```text
使用的GPU: NVIDIA GeForce RTX 5070 Ti

无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 8.69秒
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
处理时间: 3.51秒
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
处理时间: 8.92秒
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
处理时间: 8.02秒
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
处理时间: 20.61秒
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
处理时间: 14.89秒
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
处理时间: 8.13秒
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
处理时间: 24.07秒
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
处理时间: 15.94秒
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
处理时间: 13.84秒
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
处理时间: 5.56秒
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
处理时间: 8.93秒
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
处理时间: 16.31秒
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
处理时间: 18.66秒
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
处理时间: 15.12秒
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
处理时间: 35.61秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 转向正北
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
处理时间: 11.03秒
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
处理时间: 10.04秒
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
处理时间: 15.89秒
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
模型输出: {
  "mode": "turn_to",
  "action": "yaw_change",
  "angle": 270.0
}
处理时间: 27.66秒
处理后的指令:
{
  "mode": "turn_to",
  "action": "yaw_change",
  "angle": 270.0
}
与期待输出匹配: ✗

模拟发送到Redis:
redis-cli set drone_command '{"mode": "turn_to", "action": "yaw_change", "angle": 270.0}'

测试指令: 向左转45度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-45.0}}]
处理时间: 11.89秒
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
处理时间: 9.15秒
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
处理时间: 6.00秒
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
处理时间: 13.77秒
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
处理时间: 24.89秒
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
模型输出: \`\`\`json
[{"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
\`\`\`
处理时间: 66.08秒
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
处理时间: 10.62秒
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
模型输出: 
处理时间: 34.83秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 7.28秒
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
处理时间: 16.43秒
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
处理时间: 22.95秒
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
模型输出: 
处理时间: 45.16秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 12.22秒
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
模型输出: [{"action": "take_off", "params": {"height": 1.0}}, {"action": "direction_move", "params": {"orientation": "forward", "distance": 3.0}}, {"action": "direction_move", "params": {"orientation": "right", "distance": 2.0}}, {"action": "direction_move", "params": {"orientation": "backward", "distance": 3.0}}, {"action": "direction_move", "params": {"orientation": "left", "distance": 2.0}}, {"action": "land"}]
处理时间: 19.50秒
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
处理时间: 18.88秒
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
处理时间: 14.54秒
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
处理时间: 19.93秒
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
处理时间: 15.56秒
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
模型输出: [
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
处理时间: 15.53秒
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
模型输出: 
处理时间: 46.92秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 向前0.5m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
处理时间: 6.81秒
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
处理时间: 11.85秒
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
处理时间: 20.21秒
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
总测试时间: 762.49秒
匹配率: 88.37% (38/43)
============================================================
总测试时间: 762.49秒
匹配率: 88.37% (38/43)
```

