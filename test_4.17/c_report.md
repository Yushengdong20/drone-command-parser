测试模式: 完整测试
测试指令数量: 43

=== 测试配置: 温度 0.0 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.44秒
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

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 8.46秒
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
处理时间: 13.10秒
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

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 13.28秒
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
处理时间: 9.98秒
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
处理时间: 12.61秒
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
处理时间: 16.99秒
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
处理时间: 11.20秒
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
处理时间: 10.49秒
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
处理时间: 6.54秒
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
处理时间: 16.70秒
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
处理时间: 22.93秒
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
处理时间: 13.39秒
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
处理时间: 15.38秒
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
处理时间: 17.62秒
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
处理时间: 12.69秒
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
处理时间: 14.69秒
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
处理时间: 10.81秒
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
处理时间: 11.12秒
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
处理时间: 10.54秒
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
处理时间: 7.50秒
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
处理时间: 11.68秒
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
处理时间: 12.01秒
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
处理时间: 10.23秒
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
处理时间: 12.90秒
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
处理时间: 15.96秒
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
处理时间: 10.07秒
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
处理时间: 16.95秒
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
处理时间: 7.39秒
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
处理时间: 9.88秒
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
处理时间: 33.61秒
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
处理时间: 41.18秒
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
处理时间: 26.07秒
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
处理时间: 22.92秒
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
处理时间: 21.48秒
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
处理时间: 9.13秒
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
处理时间: 18.75秒
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
处理时间: 25.63秒
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
处理时间: 10.05秒
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
处理时间: 7.97秒
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
处理时间: 15.63秒
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
总测试时间: 627.04秒
匹配率: 100.00% (43/43)
============================================================

=== 测试配置: 温度 0.3 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 13.38秒
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
处理时间: 8.41秒
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
处理时间: 8.46秒
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
处理时间: 13.09秒
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
处理时间: 9.64秒
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
处理时间: 13.26秒
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
处理时间: 10.00秒
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
处理时间: 12.62秒
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
处理时间: 16.98秒
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
处理时间: 11.26秒
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
处理时间: 10.51秒
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
处理时间: 6.54秒
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
处理时间: 16.69秒
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
处理时间: 30.02秒
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
处理时间: 13.44秒
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
处理时间: 15.41秒
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
处理时间: 17.65秒
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
处理时间: 12.70秒
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
处理时间: 14.67秒
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
处理时间: 10.83秒
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
处理时间: 11.17秒
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
处理时间: 10.56秒
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
处理时间: 7.54秒
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
处理时间: 11.71秒
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
处理时间: 8.27秒
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
处理时间: 10.23秒
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
处理时间: 12.91秒
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

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
处理时间: 10.09秒
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
处理时间: 17.00秒
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
处理时间: 7.43秒
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
处理时间: 9.90秒
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
处理时间: 30.08秒
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
处理时间: 42.22秒
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
处理时间: 26.13秒
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
处理时间: 23.38秒
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
处理时间: 24.77秒
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
处理时间: 9.11秒
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
处理时间: 18.72秒
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
处理时间: 25.61秒
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
处理时间: 12.06秒
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
处理时间: 7.99秒
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
处理时间: 15.64秒
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
总测试时间: 634.08秒
匹配率: 100.00% (43/43)
============================================================

=== 测试配置: 温度 0.7 ===
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

测试指令: 起飞到2米
期待输出: [{"action":"take_off","params":{"height":2.0}}]
模型输出: [{"action":"take_off","params":{"height":2.0}}]
处理时间: 8.47秒
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
处理时间: 13.13秒
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

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 13.31秒
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
处理时间: 10.03秒
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
处理时间: 12.62秒
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
处理时间: 16.99秒
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
处理时间: 13.50秒
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
处理时间: 10.52秒
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
处理时间: 6.56秒
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
处理时间: 18.02秒
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
处理时间: 24.65秒
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
处理时间: 13.38秒
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
处理时间: 15.42秒
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
处理时间: 20.63秒
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
处理时间: 12.70秒
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
处理时间: 14.68秒
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
处理时间: 10.84秒
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
处理时间: 11.18秒
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
处理时间: 10.54秒
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
处理时间: 7.51秒
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
处理时间: 10.22秒
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
处理时间: 8.26秒
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
处理时间: 10.23秒
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
处理时间: 12.13秒
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
处理时间: 15.93秒
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
处理时间: 10.07秒
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
处理时间: 16.97秒
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
处理时间: 7.41秒
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
处理时间: 9.91秒
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
处理时间: 30.06秒
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
处理时间: 42.23秒
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
处理时间: 26.12秒
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
处理时间: 24.04秒
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
处理时间: 21.48秒
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
处理时间: 9.10秒
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
处理时间: 18.71秒
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
处理时间: 25.62秒
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
处理时间: 10.05秒
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
处理时间: 7.97秒
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
处理时间: 15.61秒
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
总测试时间: 628.31秒
匹配率: 100.00% (43/43)
============================================================

=== 测试配置: 温度 1.0 ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 15.54秒
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
处理时间: 8.17秒
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
处理时间: 8.46秒
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
处理时间: 13.09秒
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

测试指令: 向后3m
期待输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
模型输出: [{"action":"direction_move","params":{"orientation":"backward","distance":3.0}}]
处理时间: 13.27秒
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
处理时间: 10.02秒
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
处理时间: 12.62秒
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
处理时间: 17.01秒
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
处理时间: 13.51秒
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
处理时间: 10.51秒
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
处理时间: 6.55秒
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
处理时间: 16.71秒
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
处理时间: 22.95秒
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
处理时间: 11.85秒
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
处理时间: 13.88秒
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
处理时间: 17.64秒
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
处理时间: 12.69秒
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
处理时间: 15.55秒
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
处理时间: 10.84秒
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
处理时间: 11.18秒
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
处理时间: 10.54秒
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
处理时间: 7.52秒
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
处理时间: 11.66秒
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
处理时间: 8.25秒
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
处理时间: 10.24秒
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
处理时间: 12.89秒
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
处理时间: 15.94秒
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
处理时间: 10.07秒
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
处理时间: 17.00秒
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
处理时间: 7.51秒
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
处理时间: 9.89秒
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
处理时间: 30.01秒
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
处理时间: 33.64秒
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
处理时间: 26.13秒
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
处理时间: 21.28秒
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
处理时间: 21.52秒
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
处理时间: 9.10秒
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
处理时间: 18.75秒
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
处理时间: 25.64秒
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
处理时间: 10.05秒
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
处理时间: 6.26秒
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
处理时间: 16.54秒
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
总测试时间: 612.14秒
匹配率: 100.00% (43/43)
============================================================

性能测试报告已保存到: g_report\temperature_test_report_full.md

最快配置: 温度 1.0
总处理时间: 612.11秒
最高准确率配置: 温度 0.0
匹配率: 100.00%
