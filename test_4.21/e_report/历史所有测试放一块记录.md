# 无人机指令解析器性能测试报告

## 测试配置

### qwen3.5:latest (默认配置) + 详细提示词

- 模型: qwen3.5:latest
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:latest (默认配置) + 简洁提示词

- 模型: qwen3.5:latest
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:latest (高温度) + 详细提示词

- 模型: qwen3.5:latest
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.7,
  "top\_p": 0.9,
  "max\_new\_tokens": 500
  }

### qwen3.5:latest (高温度) + 简洁提示词

- 模型: qwen3.5:latest
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.7,
  "top\_p": 0.9,
  "max\_new\_tokens": 500
  }

### qwen3.5:latest (大上下文 8192) + 详细提示词

- 模型: qwen3.5:latest
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 8192,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:latest (大上下文 8192) + 简洁提示词

- 模型: qwen3.5:latest
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 8192,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (默认配置) + 详细提示词

- 模型: qwen3.5:0.8b
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (默认配置) + 简洁提示词

- 模型: qwen3.5:0.8b
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (高温度) + 详细提示词

- 模型: qwen3.5:0.8b
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.7,
  "top\_p": 0.9,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (高温度) + 简洁提示词

- 模型: qwen3.5:0.8b
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 2048,
  "temperature": 0.7,
  "top\_p": 0.9,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (大上下文 8192) + 详细提示词

- 模型: qwen3.5:0.8b
- 提示词: 详细提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 8192,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

### qwen3.5:0.8b (大上下文 8192) + 简洁提示词

- 模型: qwen3.5:0.8b
- 提示词: 简洁提示词
- 配置: {
  "main\_gpu": 0,
  "tensor\_split": \[
  1,
  0
  ],
  "num\_ctx": 8192,
  "temperature": 0.0,
  "top\_p": 0.1,
  "max\_new\_tokens": 500
  }

## 性能数据

| 配置                                 | 提示词   | 起飞    | 降落    | 向后2m   | 起飞，向后2m，然后降落 | 起飞到2米，然后向前飞1米，最后降落 | 平均时间   |
| ---------------------------------- | ----- | ----- | ----- | ------ | ------------ | ------------------ | ------ |
| qwen3.5:latest (默认配置) + 详细提示词      | 详细提示词 | 9.68  | 11.52 | 7.23   | 9.86         | 13.43              | 10.34  |
| qwen3.5:latest (默认配置) + 简洁提示词      | 简洁提示词 | 5.98  | 10.54 | 12.47  | 4.32         | 5.44               | 7.75   |
| qwen3.5:latest (高温度) + 详细提示词       | 详细提示词 | 15.96 | 13.53 | 6.87   | 65.14        | 19.15              | 24.13  |
| qwen3.5:latest (高温度) + 简洁提示词       | 简洁提示词 | 18.84 | 3.41  | 6.76   | 6.35         | 4.01               | 7.88   |
| qwen3.5:latest (大上下文 8192) + 详细提示词 | 详细提示词 | 10.09 | 11.52 | 7.25   | 9.87         | 16.11              | 10.97  |
| qwen3.5:latest (大上下文 8192) + 简洁提示词 | 简洁提示词 | 5.96  | 10.69 | 12.54  | 4.32         | 5.42               | 7.78   |
| qwen3.5:0.8b (默认配置) + 详细提示词        | 详细提示词 | 4.57  | 2.00  | 1.81   | 1.98         | 3.27               | 2.72   |
| qwen3.5:0.8b (默认配置) + 简洁提示词        | 简洁提示词 | 2.18  | 9.57  | 10.45  | 1.82         | 9.64               | 6.73   |
| qwen3.5:0.8b (高温度) + 详细提示词         | 详细提示词 | 2.25  | 3.15  | 3.12   | 1.86         | 1.79               | 2.43   |
| qwen3.5:0.8b (高温度) + 简洁提示词         | 简洁提示词 | 3.96  | 2.66  | 4.38   | 3.04         | 14.72              | 5.75   |
| qwen3.5:0.8b (大上下文 8192) + 详细提示词   | 详细提示词 | 4.19  | 2.19  | 1.80   | 1.99         | 3.27               | 2.69   |
| qwen3.5:0.8b (大上下文 8192) + 简洁提示词   | 简洁提示词 | 2.20  | 61.09 | 414.56 | 1.80         | 101.28             | 116.19 |

## 性能总结

- qwen3.5:latest (默认配置) + 详细提示词: 总时间 = 51.71秒, 平均时间 = 10.34秒
- qwen3.5:latest (默认配置) + 简洁提示词: 总时间 = 38.75秒, 平均时间 = 7.75秒
- qwen3.5:latest (高温度) + 详细提示词: 总时间 = 120.64秒, 平均时间 = 24.13秒
- qwen3.5:latest (高温度) + 简洁提示词: 总时间 = 39.39秒, 平均时间 = 7.88秒
- qwen3.5:latest (大上下文 8192) + 详细提示词: 总时间 = 54.83秒, 平均时间 = 10.97秒
- qwen3.5:latest (大上下文 8192) + 简洁提示词: 总时间 = 38.92秒, 平均时间 = 7.78秒
- qwen3.5:0.8b (默认配置) + 详细提示词: 总时间 = 13.62秒, 平均时间 = 2.72秒
- qwen3.5:0.8b (默认配置) + 简洁提示词: 总时间 = 33.66秒, 平均时间 = 6.73秒
- qwen3.5:0.8b (高温度) + 详细提示词: 总时间 = 12.17秒, 平均时间 = 2.43秒
- qwen3.5:0.8b (高温度) + 简洁提示词: 总时间 = 28.77秒, 平均时间 = 5.75秒
- qwen3.5:0.8b (大上下文 8192) + 详细提示词: 总时间 = 13.44秒, 平均时间 = 2.69秒
- qwen3.5:0.8b (大上下文 8192) + 简洁提示词: 总时间 = 580.93秒, 平均时间 = 116.19秒

## 最佳配置分析

**最佳配置组合**: qwen3.5:0.8b (高温度) + 详细提示词&#x20;
**平均处理时间**: 2.43秒

### 变量控制分析

#### 1. 模型对比

- qwen3.5:latest: 10.34秒
- qwen3.5:0.8b: 2.72秒

#### 2. 温度对比

- 默认温度 (0.0): 10.34秒
- 高温度 (0.7): 24.13秒

#### 3. 上下文对比

- 默认上下文 (2048): 10.34秒
- 大上下文 (8192): 10.97秒

#### 4. 提示词对比

## 测试日志

````
=== 测试配置: qwen3.5:latest (默认配置) + 详细提示词 ===
测试指令: 起飞
处理时间: 9.68秒
模型输出: {"action":"take_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 11.52秒
模型输出: {"action":"land"}
测试指令: 向后2m
处理时间: 7.23秒
模型输出: {"action":"direction_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 9.86秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 13.43秒
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
=== 测试配置: qwen3.5:latest (默认配置) + 简洁提示词 ===
测试指令: 起飞
处理时间: 5.98秒
模型输出: {"action":"take_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 10.54秒
模型输出: {"action":"land"}
测试指令: 向后2m
处理时间: 12.47秒
模型输出: {"action":"direction_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 4.32秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 5.44秒
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
=== 测试配置: qwen3.5:latest (高温度) + 详细提示词 ===
测试指令: 起飞
处理时间: 15.96秒
模型输出: {"action":"take_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 13.53秒
模型输出: {"action":"land"}
测试指令: 向后2m
处理时间: 6.87秒
模型输出: {"action":"direction_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 65.14秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 19.15秒
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
=== 测试配置: qwen3.5:latest (高温度) + 简洁提示词 ===
测试指令: 起飞
处理时间: 18.84秒
模型输出: {"action":"take_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 3.41秒
模型输出: ```json
{"action":"land"}
````

测试指令: 向后2m
处理时间: 6.76秒
模型输出: {"action":"direction\_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 6.35秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 4.01秒
模型输出: \[{"action":"take\_off","params":{"height":2.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
\=== 测试配置: qwen3.5:latest (大上下文 8192) + 详细提示词 ===
测试指令: 起飞
处理时间: 10.09秒
模型输出: {"action":"take\_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 11.52秒
模型输出: {"action":"land"}
测试指令: 向后2m
处理时间: 7.25秒
模型输出: {"action":"direction\_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 9.87秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 16.11秒
模型输出: \[{"action":"take\_off","params":{"height":2.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
\=== 测试配置: qwen3.5:latest (大上下文 8192) + 简洁提示词 ===
测试指令: 起飞
处理时间: 5.96秒
模型输出: {"action":"take\_off","params":{"height":1.0}}
测试指令: 降落
处理时间: 10.69秒
模型输出: {"action":"land"}
测试指令: 向后2m
处理时间: 12.54秒
模型输出: {"action":"direction\_move","params":{"orientation":"backward","distance":2.0}}
测试指令: 起飞，向后2m，然后降落
处理时间: 4.32秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 5.42秒
模型输出: \[{"action":"take\_off","params":{"height":2.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
\=== 测试配置: qwen3.5:0.8b (默认配置) + 详细提示词 ===
测试指令: 起飞
处理时间: 4.57秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 降落
处理时间: 2.00秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 向后2m
处理时间: 1.81秒
模型输出: \`\`\`json
\[{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}}]

````
测试指令: 起飞，向后2m，然后降落
处理时间: 1.98秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 3.27秒
模型输出: [{"action":"take_off","params":{"height":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
=== 测试配置: qwen3.5:0.8b (默认配置) + 简洁提示词 ===
测试指令: 起飞
处理时间: 2.18秒
模型输出: ```json
{
  "action": [
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
}
````

测试指令: 降落
处理时间: 9.57秒
模型输出:
测试指令: 向后2m
处理时间: 10.45秒
模型输出:
测试指令: 起飞，向后2m，然后降落
处理时间: 1.82秒
模型输出: \`\`\`json
\[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]

````
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 9.64秒
模型输出: 
=== 测试配置: qwen3.5:0.8b (高温度) + 详细提示词 ===
测试指令: 起飞
处理时间: 2.25秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 降落
处理时间: 3.15秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 向后2m
处理时间: 3.12秒
模型输出: ```json
[{"action":"direction_move","params":{"orientation":"down","distance":2.0}}]
````

测试指令: 起飞，向后2m，然后降落
处理时间: 1.86秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 1.79秒
模型输出: \`\`\`json
\[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]

````
=== 测试配置: qwen3.5:0.8b (高温度) + 简洁提示词 ===
测试指令: 起飞
处理时间: 3.96秒
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
````

测试指令: 降落
处理时间: 2.66秒
模型输出: \`\`\`json
{
"action": "take\_off",
"params": {
"height": 1.0
},
"action": "direction\_move",
"params": {
"orientation": "backward",
"distance": 2.0
},
"action": "land"
}

````
测试指令: 向后2m
处理时间: 4.38秒
模型输出: ```json
{
  "action": "direction_move",
  "params": {
    "distance": 2.0
  }
}
````

测试指令: 起飞，向后2m，然后降落
处理时间: 3.04秒
模型输出: \`\`\`json
\[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]

````
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 14.72秒
模型输出: 
=== 测试配置: qwen3.5:0.8b (大上下文 8192) + 详细提示词 ===
测试指令: 起飞
处理时间: 4.19秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 降落
处理时间: 2.19秒
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
测试指令: 向后2m
处理时间: 1.80秒
模型输出: ```json
[{"action":"direction_move","params":{"orientation":"backward","distance":2.0}}]
````

测试指令: 起飞，向后2m，然后降落
处理时间: 1.99秒
模型输出: \[{"action":"take\_off","params":{"height":1.0}},{"action":"direction\_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 3.27秒
模型输出: \[{"action":"take\_off","params":{"height":2.0}},{"action":"direction\_move","params":{"orientation":"forward","distance":1.0}},{"action":"land"}]
\=== 测试配置: qwen3.5:0.8b (大上下文 8192) + 简洁提示词 ===
测试指令: 起飞
处理时间: 2.20秒
模型输出: \`\`\`json
{
"action": \[
{
"action": "take\_off",
"params": {
"height": 1.0
}
},
{
"action": "direction\_move",
"params": {
"orientation": "backward",
"distance": 2.0
}
},
{
"action": "land"
}
]
}

````
测试指令: 降落
处理时间: 61.09秒
模型输出: 
测试指令: 向后2m
处理时间: 414.56秒
模型输出: 
测试指令: 起飞，向后2m，然后降落
处理时间: 1.80秒
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
````

测试指令: 起飞到2米，然后向前飞1米，最后降落
处理时间: 101.28秒
模型输出:

```
```

