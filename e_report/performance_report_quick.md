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
  "num_ctx": 2048,
  "temperature": 0.0,
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
  "num_ctx": 2048,
  "temperature": 0.0,
  "top_p": 0.1,
  "max_new_tokens": 500
}

## 性能数据

### 基础动作 - 起飞降落

| 模型 | 起飞 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| qwen3.5:latest | 13.72 | 8.61 | 22.33 | 100.00% |
| qwen3.5:0.8b | 4.11 | 1.51 | 5.62 | 100.00% |
### 基础动作 - 方向移动

| 模型 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| qwen3.5:latest | 9.90 | 9.90 | 100.00% |
| qwen3.5:0.8b | 1.73 | 1.73 | 100.00% |
### 组合指令 - 简单序列

| 模型 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| qwen3.5:latest | 49.52 | 49.52 | 100.00% |
| qwen3.5:0.8b | 2.82 | 2.82 | 100.00% |

### 汇总

| 模型 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| qwen3.5:latest | 22.33 | 9.90 | 49.52 | 81.75 | 100.00% |
| qwen3.5:0.8b | 5.62 | 1.73 | 2.82 | 10.16 | 100.00% |

## 性能总结

- qwen3.5:latest: 总时间 = 81.75秒, 匹配率 = 100.00% (4/4)
- qwen3.5:0.8b: 总时间 = 10.16秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: qwen3.5:0.8b
**总处理时间**: 10.16秒
**最高准确率配置**: qwen3.5:latest
**匹配率**: 100.00%

### 模型对比分析

- qwen3.5:latest: 总时间 = 81.75秒, 匹配率 = 100.00% (4/4)
- qwen3.5:0.8b: 总时间 = 10.16秒, 匹配率 = 100.00% (4/4)

## 测试日志

```
=== 测试配置: qwen3.5:latest ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.72秒
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
处理时间: 8.61秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 9.90秒
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

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 49.52秒
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

============================================================
测试完成！
总测试时间: 81.75秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 81.75秒
匹配率: 100.00% (4/4)
=== 测试配置: qwen3.5:0.8b ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 4.11秒
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
处理时间: 1.51秒
处理后的指令:
[
  {
    "action": "land"
  }
]
与期待输出匹配: ✓

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "land"}'

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 1.73秒
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

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
处理时间: 2.82秒
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

============================================================
测试完成！
总测试时间: 10.17秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 10.17秒
匹配率: 100.00% (4/4)
```
