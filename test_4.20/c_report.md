测试模式: 完整测试
测试指令数量: 43

=== 测试配置: qwen3.5:latest ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 9.68秒
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
处理时间: 6.61秒
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
处理时间: 7.20秒
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
处理时间: 8.81秒
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
处理时间: 6.05秒
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
处理时间: 14.54秒
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
处理时间: 8.36秒
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
处理时间: 11.12秒
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
处理时间: 11.98秒
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
处理时间: 9.42秒
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
处理时间: 6.22秒
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
处理时间: 8.06秒
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
处理时间: 10.58秒
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
处理时间: 48.44秒
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
处理时间: 28.07秒
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
处理时间: 12.25秒
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
处理时间: 12.81秒
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
处理时间: 14.76秒
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
处理时间: 22.60秒
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
处理时间: 15.49秒
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
处理时间: 16.95秒
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
处理时间: 10.19秒
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
处理时间: 9.78秒
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
处理时间: 14.47秒
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
处理时间: 28.06秒
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
处理时间: 10.70秒
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
处理时间: 13.63秒
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
处理时间: 36.03秒
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
处理时间: 51.09秒
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
处理时间: 18.67秒
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
处理时间: 13.24秒
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
处理时间: 9.12秒
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
处理时间: 26.54秒
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
处理时间: 20.76秒
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
处理时间: 36.63秒
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
处理时间: 18.95秒
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
处理时间: 14.11秒
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
处理时间: 18.53秒
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
处理时间: 41.37秒
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
处理时间: 34.12秒
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
处理时间: 16.85秒
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
处理时间: 11.32秒
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
处理时间: 16.44秒
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
总测试时间: 760.61秒
匹配率: 100.00% (43/43)
============================================================

=== 测试配置: qwen3.5:0.8b ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 18.59秒
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
处理时间: 2.27秒
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
模型输出: 
处理时间: 891.94秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞到5米
期待输出: [{"action":"take_off","params":{"height":5.0}}]
模型输出: [{"action":"take_off","params":{"height":5.0}}]
处理时间: 1.96秒
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
处理时间: 1.56秒
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
处理时间: 2.14秒
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
处理时间: 3.43秒
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
处理时间: 1.53秒
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
处理时间: 1.88秒
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
处理时间: 1.78秒
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
处理时间: 1.56秒
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
处理时间: 2.51秒
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
处理时间: 2.37秒
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
处理时间: 1.97秒
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
模型输出: 
处理时间: 875.36秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 机头朝西
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":270.0}}]
处理时间: 2.04秒
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
处理时间: 842.86秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 转向正东
期待输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}}]
处理时间: 2.81秒
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
处理时间: 1.65秒
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
处理时间: 2.05秒
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
处理时间: 1.60秒
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
处理时间: 78.32秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 顺时针转90度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":90.0}}]
模型输出: 
处理时间: 846.07秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 逆时针转60度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
模型输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":-60.0}}]
处理时间: 1.93秒
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
处理时间: 2.06秒
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
处理时间: 2.44秒
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
模型输出: [{"action":"turn_to","params":{"mode":"turn_to","angle":180.0}}]
处理时间: 3.59秒
处理后的指令:
[
  {
    "action": "turn_to",
    "params": {
      "mode": "turn_to",
      "angle": 180.0
    }
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "turn_to", "params": {"mode": "turn_to", "angle": 180.0}}'

测试指令: 起飞，向前2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
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

测试指令: 起飞，向后2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"backward","distance":2.0}},{"action":"land"}]
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
模型输出: 
处理时间: 846.42秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，向右2m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
处理时间: 4.98秒
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
模型输出: [{"action":"take_off","params":{"height":2.0}},"action":"direction_move","params":{"orientation":"forward","distance":1.0}},"action":"land"}
处理时间: 2.98秒
错误: 解析指令失败
详情: Expecting ',' delimiter: line 1 column 56 (char 55)

测试指令: 起飞，升高2m，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":2.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 2.04秒
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
处理时间: 5.82秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}},"action":"direction_move","params":{"orientation":"forward","distance":2.0},"action":"yaw_change","params":{"mode":"turn_by","angle":-90.0}}]
处理时间: 2.95秒
错误: 解析指令失败
详情: Expecting ',' delimiter: line 1 column 56 (char 55)

测试指令: 起飞，机头朝东，向前5m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
处理时间: 1.87秒
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
处理时间: 2.49秒
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
模型输出: 
处理时间: 845.85秒
错误: 解析指令失败
详情: Expecting value: line 1 column 1 (char 0)

测试指令: 起飞，升高1m，原地转一圈，降低1m，然后降落
期待输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
模型输出: [{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
处理时间: 3.17秒
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
处理时间: 1.95秒
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
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 1.59秒
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

测试指令: 向右转0度
期待输出: [{"action":"yaw_change","params":{"mode":"turn_by","angle":0.0}}]
模型输出: [{"action":"turn_to","params":{"angle":0.0}}]
处理时间: 2.27秒
处理后的指令:
[
  {
    "action": "turn_to",
    "params": {
      "angle": 0.0
    }
  }
]
与期待输出匹配: ✗

模拟发送到Redis:
步骤 1: redis-cli set drone_command '{"action": "turn_to", "params": {"angle": 0.0}}'

============================================================
测试完成！
总测试时间: 5329.03秒
匹配率: 67.44% (29/43)
============================================================

=== 测试配置: qwen3.5:2b ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 8.01秒
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
处理时间: 2.43秒
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
处理时间: 3.09秒
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
处理时间: 3.21秒
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
处理时间: 2.05秒
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
处理时间: 3.00秒
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
处理时间: 3.34秒
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
处理时间: 2.64秒
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
处理时间: 3.24秒
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
处理时间: 2.85秒
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
处理时间: 3.13秒
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
处理时间: 2.48秒
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
处理时间: 3.46秒
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
处理时间: 3.32秒
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
模型输出: ```json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":180.0}}]
```
处理时间: 3.76秒
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
处理时间: 3.23秒
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
模型输出: ```json
[{"action":"yaw_change","params":{"mode":"turn_to","angle":0.0}}]
```
处理时间: 2.79秒
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
处理时间: 3.11秒
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
处理时间: 2.66秒
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
处理时间: 3.94秒
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
处理时间: 3.76秒
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
处理时间: 3.87秒
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
处理时间: 3.16秒
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
处理时间: 3.20秒
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
处理时间: 3.42秒
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
处理时间: 4.61秒
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
处理时间: 3.30秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"forward","distance":2.0}},{"action":"land"}]
```
处理时间: 2.57秒
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
处理时间: 2.81秒
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
处理时间: 3.44秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"right","distance":2.0}},{"action":"land"}]
```
处理时间: 3.57秒
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
处理时间: 3.39秒
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
处理时间: 4.06秒
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
处理时间: 4.74秒
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
处理时间: 3.55秒
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
处理时间: 4.53秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_to","angle":90.0}},{"action":"direction_move","params":{"orientation":"forward","distance":5.0}},{"action":"land"}]
```
处理时间: 2.89秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":180.0}},{"action":"direction_move","params":{"orientation":"forward","distance":3.0}},{"action":"land"}]
```
处理时间: 4.03秒
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
处理时间: 9.79秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":1.0}},{"action":"direction_move","params":{"orientation":"up","distance":1.0}},{"action":"yaw_change","params":{"mode":"turn_by","angle":360.0}},{"action":"direction_move","params":{"orientation":"down","distance":1.0}},{"action":"land"}]
```
处理时间: 3.38秒
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
模型输出: ```json
[{"action":"direction_move","params":{"orientation":"forward","distance":0.5}}]
```
处理时间: 2.66秒
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
模型输出: ```json
[{"action":"take_off","params":{"height":0.5}}]
```
处理时间: 2.86秒
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
处理时间: 5.06秒
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
总测试时间: 154.43秒
匹配率: 100.00% (43/43)
============================================================

=== 测试配置: qwen3.5:4b ===
无人机指令解析器测试
============================================================
开始测试...
============================================================

测试指令: 起飞
期待输出: [{"action":"take_off","params":{"height":1.0}}]
模型输出: [{"action":"take_off","params":{"height":1.0}}]
处理时间: 24.31秒
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
处理时间: 6.68秒
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
处理时间: 17.06秒
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
处理时间: 6.87秒
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
处理时间: 10.49秒
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
处理时间: 13.63秒
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
处理时间: 15.79秒
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
处理时间: 28.43秒
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
处理时间: 14.63秒
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
处理时间: 9.29秒
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
处理时间: 10.09秒
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
处理时间: 22.55秒
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
处理时间: 39.48秒
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
处理时间: 7.94秒
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
处理时间: 16.69秒
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
处理时间: 19.88秒
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
处理时间: 15.82秒
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
处理时间: 8.04秒
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
处理时间: 17.68秒
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
处理时间: 32.80秒
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
处理时间: 7.16秒
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
处理时间: 10.72秒
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
处理时间: 12.27秒
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
处理时间: 30.09秒
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
处理时间: 11.41秒
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
处理时间: 14.64秒
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
处理时间: 20.27秒
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
处理时间: 17.79秒
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
处理时间: 21.65秒
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
处理时间: 6.60秒
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
处理时间: 16.97秒
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
处理时间: 18.56秒
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
处理时间: 24.67秒
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
处理时间: 9.52秒
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
处理时间: 15.41秒
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
处理时间: 17.98秒
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
处理时间: 16.57秒
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
处理时间: 27.19秒
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
处理时间: 11.71秒
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
处理时间: 17.47秒
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
处理时间: 26.03秒
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
总测试时间: 717.75秒
匹配率: 100.00% (43/43)
============================================================

性能测试报告已保存到: e_report\performance_report_full_001.md

最快配置: qwen3.5:2b
总处理时间: 154.37秒
最高准确率配置: qwen3.5:latest
匹配率: 100.00%
