import redis
import json
import time

def get_redis_client():
    """
    获取 Redis 客户端连接
    """
    try:
        r = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        r.ping()
        print("[OK] Redis 连接成功")
        return r
    except redis.ConnectionError:
        print("[错误] 无法连接到 Redis!")
        print("请确保 Redis 服务器在 localhost:6379 运行")
        return None

def add_to_queue(r, command):
    """
    添加指令到队列
    """
    try:
        cmd_with_metadata = {
            "command": command,
            "timestamp": time.time(),
            "sequence": 0
        }
        r.rpush("drone_command_queue", json.dumps(cmd_with_metadata))
        print(f"[OK] 已添加指令到队列: {command['action']}")
    except Exception as e:
        print(f"[错误] 添加到队列失败: {e}")

def simulate_model_outputs():
    """
    模拟大模型输出的指令
    """
    # 模拟大模型输出的指令格式
    model_outputs = [
        {"action": "take_off", "params": {"height": 1.0}},
        {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
        {"action": "direction_move", "params": {"orientation": "up", "distance": 1.0}},
        {"action": "yaw_change", "params": {"mode": "turn_to", "angle": 90.0}},
        {"action": "land"}
    ]
    return model_outputs

def main():
    """
    主函数
    """
    print("=== Redis 指令写入工具 ===")
    print("模拟大模型输出指令并添加到 Redis 队列")
    
    r = get_redis_client()
    if not r:
        return
    
    # 清空队列
    try:
        r.delete("drone_command_queue")
        print("[OK] 队列已清空")
    except Exception as e:
        print(f"[错误] 清空队列失败: {e}")
    
    # 获取模拟的模型输出
    model_outputs = simulate_model_outputs()
    
    # 逐一添加到队列
    print("\n添加指令到队列:")
    for i, command in enumerate(model_outputs, 1):
        print(f"\n{i}. 指令: {command['action']}")
        print(f"   详细: {json.dumps(command, indent=2)}")
        add_to_queue(r, command)
        time.sleep(0.5)  # 模拟处理时间
    
    # 显示队列状态
    try:
        length = r.llen("drone_command_queue")
        print(f"\n[信息] 队列长度: {length}")
        print("[信息] 所有指令已添加到队列")
    except Exception as e:
        print(f"[错误] 显示队列状态失败: {e}")
    
    print("\n=== 操作完成 ===")
    print("请运行 l_redis_reader.py 读取队列中的指令")

if __name__ == "__main__":
    try:
        import redis
        print("[OK] redis 模块已安装")
    except ImportError:
        print("[错误] redis 模块未安装！")
        print("请运行: pip install redis")
        exit(1)
    
    main()
