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

| 模型 | 起飞 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| qwen3.5:latest | 8.17 | 5.30 | 13.46 | 100.00% |
| qwen3.5:0.8b | 2.93 | 1.54 | 4.46 | 50.00% |
| qwen3.5:2b | 5.36 | 1.97 | 7.34 | 100.00% |
| qwen3.5:4b | 12.61 | 3.94 | 16.55 | 100.00% |
### 基础动作 - 方向移动

| 模型 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| qwen3.5:latest | 5.03 | 5.03 | 100.00% |
| qwen3.5:0.8b | 1.26 | 1.26 | 100.00% |
| qwen3.5:2b | 2.78 | 2.78 | 100.00% |
| qwen3.5:4b | 9.27 | 9.27 | 100.00% |
### 组合指令 - 简单序列

| 模型 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| qwen3.5:latest | 16.05 | 16.05 | 100.00% |
| qwen3.5:0.8b | 1.68 | 1.68 | 100.00% |
| qwen3.5:2b | 2.26 | 2.26 | 100.00% |
| qwen3.5:4b | 31.92 | 31.92 | 100.00% |

### 汇总

| 模型 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| qwen3.5:latest | 13.46 | 5.03 | 16.05 | 34.55 | 100.00% |
| qwen3.5:0.8b | 4.46 | 1.26 | 1.68 | 7.40 | 75.00% |
| qwen3.5:2b | 7.34 | 2.78 | 2.26 | 12.38 | 100.00% |
| qwen3.5:4b | 16.55 | 9.27 | 31.92 | 57.75 | 100.00% |

## 性能总结

- qwen3.5:latest: 总时间 = 34.55秒, 匹配率 = 100.00% (4/4)
- qwen3.5:0.8b: 总时间 = 7.40秒, 匹配率 = 75.00% (3/4)
- qwen3.5:2b: 总时间 = 12.38秒, 匹配率 = 100.00% (4/4)
- qwen3.5:4b: 总时间 = 57.75秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: qwen3.5:0.8b
**总处理时间**: 7.40秒
**最高准确率配置**: qwen3.5:latest, qwen3.5:2b, qwen3.5:4b
**匹配率**: 100.00%

### 模型对比分析

- qwen3.5:latest: 总时间 = 34.55秒, 匹配率 = 100.00% (4/4)
- qwen3.5:0.8b: 总时间 = 7.40秒, 匹配率 = 75.00% (3/4)
- qwen3.5:2b: 总时间 = 12.38秒, 匹配率 = 100.00% (4/4)
- qwen3.5:4b: 总时间 = 57.75秒, 匹配率 = 100.00% (4/4)

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
处理时间: 8.17秒
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
处理时间: 5.30秒
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
处理时间: 5.03秒
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

============================================================
测试完成！
总测试时间: 34.55秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 34.55秒
匹配率: 100.00% (4/4)
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
处理时间: 2.93秒
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
处理时间: 1.54秒
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

测试指令: 向前2m
期待输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"forward","distance":2.0}}]
处理时间: 1.26秒
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
处理时间: 1.68秒
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
总测试时间: 7.41秒
匹配率: 75.00% (3/4)
============================================================
总测试时间: 7.41秒
匹配率: 75.00% (3/4)
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
处理时间: 5.36秒
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
处理时间: 1.97秒
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

============================================================
测试完成！
总测试时间: 12.38秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 12.38秒
匹配率: 100.00% (4/4)
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
处理时间: 12.61秒
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
处理时间: 3.94秒
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
处理时间: 9.27秒
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
处理时间: 31.92秒
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
总测试时间: 57.75秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 57.75秒
匹配率: 100.00% (4/4)
```

