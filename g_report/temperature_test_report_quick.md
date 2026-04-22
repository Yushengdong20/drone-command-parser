# 无人机指令解析器温度参数测试报告

## 测试配置

### 温度 0.0
- 模型: qwen3.5:latest
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
- 模型: qwen3.5:latest
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
- 模型: qwen3.5:latest
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
- 模型: qwen3.5:latest
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
| 温度 0.0 | 19.56 | 8.42 | 27.98 | 100.00% |
| 温度 0.3 | 13.40 | 8.43 | 21.83 | 100.00% |
| 温度 0.7 | 13.37 | 8.43 | 21.80 | 100.00% |
| 温度 1.0 | 13.42 | 8.45 | 21.87 | 100.00% |
### 基础动作 - 方向移动

| 配置 | 向前2m | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 温度 0.0 | 9.62 | 9.62 | 100.00% |
| 温度 0.3 | 9.62 | 9.62 | 100.00% |
| 温度 0.7 | 9.63 | 9.63 | 100.00% |
| 温度 1.0 | 9.66 | 9.66 | 100.00% |
### 组合指令 - 简单序列

| 配置 | 起飞，向前2m，然后... | 分类总时间 | 分类匹配率 |
|------|------|----------|--------|
| 温度 0.0 | 15.97 | 15.97 | 100.00% |
| 温度 0.3 | 15.99 | 15.99 | 100.00% |
| 温度 0.7 | 16.00 | 16.00 | 100.00% |
| 温度 1.0 | 16.02 | 16.02 | 100.00% |

### 汇总

| 配置 | 基础动作 - 起飞降落 |基础动作 - 方向移动 |组合指令 - 简单序列 | 总时间 | 总匹配率 |
|------|------|------|------|----------|--------|
| 温度 0.0 | 27.98 | 9.62 | 15.97 | 53.57 | 100.00% |
| 温度 0.3 | 21.83 | 9.62 | 15.99 | 47.44 | 100.00% |
| 温度 0.7 | 21.80 | 9.63 | 16.00 | 47.43 | 100.00% |
| 温度 1.0 | 21.87 | 9.66 | 16.02 | 47.55 | 100.00% |

## 性能总结

- 温度 0.0: 总时间 = 53.57秒, 匹配率 = 100.00% (4/4)
- 温度 0.3: 总时间 = 47.44秒, 匹配率 = 100.00% (4/4)
- 温度 0.7: 总时间 = 47.43秒, 匹配率 = 100.00% (4/4)
- 温度 1.0: 总时间 = 47.55秒, 匹配率 = 100.00% (4/4)

## 最佳配置分析

**最快配置**: 温度 0.7
**总处理时间**: 47.43秒
**最高准确率配置**: 温度 0.0
**匹配率**: 100.00%

### 温度参数对比分析

- 温度 0.0: 总时间 = 53.57秒, 匹配率 = 100.00% (4/4)
- 温度 0.3: 总时间 = 47.44秒, 匹配率 = 100.00% (4/4)
- 温度 0.7: 总时间 = 47.43秒, 匹配率 = 100.00% (4/4)
- 温度 1.0: 总时间 = 47.55秒, 匹配率 = 100.00% (4/4)

## 测试日志

```
=== 测试配置: 温度 0.0 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 19.56秒
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
处理时间: 8.42秒
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
处理时间: 9.62秒
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
处理时间: 15.97秒
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
总测试时间: 53.58秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 53.58秒
匹配率: 100.00% (4/4)
=== 测试配置: 温度 0.3 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.40秒
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
处理时间: 8.43秒
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
处理时间: 9.62秒
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
处理时间: 15.99秒
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
总测试时间: 47.45秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 47.45秒
匹配率: 100.00% (4/4)
=== 测试配置: 温度 0.7 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.37秒
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
处理时间: 8.43秒
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
处理时间: 9.63秒
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
总测试时间: 47.43秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 47.43秒
匹配率: 100.00% (4/4)
=== 测试配置: 温度 1.0 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.42秒
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
处理时间: 8.45秒
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
处理时间: 9.66秒
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
处理时间: 16.02秒
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
总测试时间: 47.55秒
匹配率: 100.00% (4/4)
============================================================
总测试时间: 47.55秒
匹配率: 100.00% (4/4)
```
