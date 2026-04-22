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

| 配置 | 起飞 |降落 | 分类总时间 | 分类匹配率 |
|------|------|------|----------|--------|
| 温度 0.0 | 2.64 | 1.95 | 4.59 | 100.00% |
| 温度 0.3 | 2.65 | 1.97 | 4.62 | 100.00% |
| 温度 0.7 | 2.66 | 2.64 | 5.30 | 100.00% |
| 温度 1.0 | 2.64 | 1.96 | 4.60 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 温度 0.0 | 2.76 | 2.76 | 100.00% |
| 温度 0.3 | 2.74 | 2.74 | 100.00% |
| 温度 0.7 | 2.77 | 2.77 | 100.00% |
| 温度 1.0 | 2.78 | 2.78 | 100.00% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 温度 0.0 | 2.25 | 2.25 | 100.00% |
| 温度 0.3 | 2.26 | 2.26 | 100.00% |
| 温度 0.7 | 2.27 | 2.27 | 100.00% |
| 温度 1.0 | 2.30 | 2.30 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| 温度 0.0 | 4.59 | 2.76 | 2.25 | 9.60 | 100.00% |
| 温度 0.3 | 4.62 | 2.74 | 2.26 | 9.62 | 100.00% |
| 温度 0.7 | 5.30 | 2.77 | 2.27 | 10.34 | 100.00% |
| 温度 1.0 | 4.60 | 2.78 | 2.30 | 9.68 | 100.00% |

## 性能总结

- 温度 0.0: 总时间 = 9.60秒, 匹配率 = 100.00% (4/4)
- 温度 0.3: 总时间 = 9.62秒, 匹配率 = 100.00% (4/4)
- 温度 0.7: 总时间 = 10.34秒, 匹配率 = 100.00% (4/4)
- 温度 1.0: 总时间 = 9.68秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: 温度 0.0
**总处理时间**: 9.60秒
**最高准确率配置**: 温度 0.0, 温度 0.3, 温度 0.7, 温度 1.0
**匹配率**: 100.00%

### 温度参数对比分析

- 温度 0.0: 总时间 = 9.60秒, 匹配率 = 100.00% (4/4)
- 温度 0.3: 总时间 = 9.62秒, 匹配率 = 100.00% (4/4)
- 温度 0.7: 总时间 = 10.34秒, 匹配率 = 100.00% (4/4)
- 温度 1.0: 总时间 = 9.68秒, 匹配率 = 100.00% (4/4)

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
处理时间: 2.64秒
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

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: \`\`\`json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
\`\`\`
处理时间: 2.25秒
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
总测试时间: 9.60秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 9.60秒
匹配率: 100.00% (4/4)
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
总测试时间: 9.62秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 9.62秒
匹配率: 100.00% (4/4)
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
模型输出: \`\`\`json
[{"action":"land"}]
\`\`\`
处理时间: 2.64秒
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
处理时间: 2.77秒
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
总测试时间: 10.34秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 10.34秒
匹配率: 100.00% (4/4)
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
处理时间: 2.64秒
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

============================================================
测试完成！
总测试时间: 9.68秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 9.68秒
匹配率: 100.00% (4/4)
```

