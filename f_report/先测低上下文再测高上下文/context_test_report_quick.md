# 无人机指令解析器上下文大小测试报告

## 测试配置

### 低上下文 (2048)
- 模型: qwen3.5:latest
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 0.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 2048
}

### 高上下文 (16384)
- 模型: qwen3.5:latest
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 0.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 16384
}

## 性能数据

### 基础动作 - 起飞降落

| 配置 | 起飞 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| 低上下文 (2048) | 49.25 | 8.52 | 57.77 | 100.00% |
| 高上下文 (16384) | 16.12 | 8.36 | 24.48 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 低上下文 (2048) | 9.61 | 9.61 | 100.00% |
| 高上下文 (16384) | 9.65 | 9.65 | 100.00% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 低上下文 (2048) | 56.64 | 56.64 | 100.00% |
| 高上下文 (16384) | 16.19 | 16.19 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| 低上下文 (2048) | 57.77 | 9.61 | 56.64 | 124.02 | 100.00% |
| 高上下文 (16384) | 24.48 | 9.65 | 16.19 | 50.32 | 100.00% |

## 性能总结

- 低上下文 (2048): 总时间 = 124.02秒, 匹配率 = 100.00% (4/4)
- 高上下文 (16384): 总时间 = 50.32秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: 高上下文 (16384)
**总处理时间**: 50.32秒
**最高准确率配置**: 低上下文 (2048)
**匹配率**: 100.00%

### 上下文大小对比分析

- 低上下文 (2048): 总时间 = 124.02秒, 匹配率 = 100.00% (4/4)
- 高上下文 (16384): 总时间 = 50.32秒, 匹配率 = 100.00% (4/4)

## 测试日志

```
=== 测试配置: 低上下文 (2048) ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 49.25秒
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
处理时间: 8.52秒
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
处理时间: 9.61秒
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
处理时间: 56.64秒
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
总测试时间: 124.03秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 124.03秒
匹配率: 100.00% (4/4)
=== 测试配置: 高上下文 (16384) ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 16.12秒
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
处理时间: 8.36秒
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
处理时间: 9.65秒
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
处理时间: 16.19秒
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
总测试时间: 50.32秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 50.32秒
匹配率: 100.00% (4/4)
```
