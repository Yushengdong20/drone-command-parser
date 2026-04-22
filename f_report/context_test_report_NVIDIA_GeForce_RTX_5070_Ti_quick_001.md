# 无人机指令解析器上下文大小测试报告

## 测试配置

### 上下文 (2048)
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 2048
}

### 上下文 (4096)
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 4096
}

### 上下文 (8192)
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 8192
}

### 上下文 (16384)
- 模型: qwen3.5:2b
- 提示词: DEFAULT_PROMPT
- 配置: {
  "main_gpu": 0,
  "tensor_split": [
    1,
    0
  ],
  "temperature": 1.0,
  "top_p": 0.1,
  "max_new_tokens": 500,
  "num_ctx": 16384
}

## 性能数据

### 基础动作 - 起飞降落

| 配置 | 起飞 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| 上下文 (2048) | 4.68 | 1.96 | 6.64 | 100.00% |
| 上下文 (4096) | 4.71 | 1.96 | 6.68 | 100.00% |
| 上下文 (8192) | 4.69 | 1.96 | 6.65 | 100.00% |
| 上下文 (16384) | 4.80 | 1.95 | 6.75 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 上下文 (2048) | 2.74 | 2.74 | 100.00% |
| 上下文 (4096) | 2.74 | 2.74 | 100.00% |
| 上下文 (8192) | 2.75 | 2.75 | 100.00% |
| 上下文 (16384) | 2.75 | 2.75 | 100.00% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 上下文 (2048) | 2.26 | 2.26 | 100.00% |
| 上下文 (4096) | 2.26 | 2.26 | 100.00% |
| 上下文 (8192) | 2.28 | 2.28 | 100.00% |
| 上下文 (16384) | 2.27 | 2.27 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| 上下文 (2048) | 6.64 | 2.74 | 2.26 | 11.63 | 100.00% |
| 上下文 (4096) | 6.68 | 2.74 | 2.26 | 11.68 | 100.00% |
| 上下文 (8192) | 6.65 | 2.75 | 2.28 | 11.69 | 100.00% |
| 上下文 (16384) | 6.75 | 2.75 | 2.27 | 11.76 | 100.00% |

## 性能总结

- 上下文 (2048): 总时间 = 11.63秒, 匹配率 = 100.00% (4/4)
- 上下文 (4096): 总时间 = 11.68秒, 匹配率 = 100.00% (4/4)
- 上下文 (8192): 总时间 = 11.69秒, 匹配率 = 100.00% (4/4)
- 上下文 (16384): 总时间 = 11.76秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: 上下文 (2048)
**总处理时间**: 11.63秒
**最高准确率配置**: 上下文 (2048), 上下文 (4096), 上下文 (8192), 上下文 (16384)
**匹配率**: 100.00%

### 上下文大小对比分析

- 上下文 (2048): 总时间 = 11.63秒, 匹配率 = 100.00% (4/4)
- 上下文 (4096): 总时间 = 11.68秒, 匹配率 = 100.00% (4/4)
- 上下文 (8192): 总时间 = 11.69秒, 匹配率 = 100.00% (4/4)
- 上下文 (16384): 总时间 = 11.76秒, 匹配率 = 100.00% (4/4)

## 测试日志

### === 测试配置: 上下文 (2048) ===

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
处理时间: 4.68秒
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
总测试时间: 11.63秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 11.63秒
匹配率: 100.00% (4/4)
```

### === 测试配置: 上下文 (4096) ===

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
处理时间: 4.71秒
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
总测试时间: 11.68秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 11.68秒
匹配率: 100.00% (4/4)
```

### === 测试配置: 上下文 (8192) ===

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
处理时间: 4.69秒
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

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.28秒
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
总测试时间: 11.69秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 11.69秒
匹配率: 100.00% (4/4)
```

### === 测试配置: 上下文 (16384) ===

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
处理时间: 4.80秒
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

============================================================
测试完成！
总测试时间: 11.77秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 11.77秒
匹配率: 100.00% (4/4)
```

