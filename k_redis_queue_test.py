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

def read_from_queue(r):
    """
    从队列读取数据
    """
    try:
        data = r.lpop("drone_command_queue")
        if data:
            return json.loads(data)
        return None
    except Exception as e:
        print(f"[错误] 从队列读取失败: {e}")
        return None

def show_queue_status(r):
    """
    显示队列状态
    """
    try:
        length = r.llen("drone_command_queue")
        print(f"[信息] 队列长度: {length}")
        
        if length > 0:
            print("\n队列内容:")
            items = r.lrange("drone_command_queue", 0, -1)
            for i, item in enumerate(items, 1):
                try:
                    data = json.loads(item)
                    print(f"  {i}. {data['command']['action']} (时间戳: {data['timestamp']})")
                except:
                    print(f"  {i}. 无效数据")
    except Exception as e:
        print(f"[错误] 显示队列状态失败: {e}")

def clear_queue(r):
    """
    清空队列
    """
    try:
        r.delete("drone_command_queue")
        print("[OK] 队列已清空")
    except Exception as e:
        print(f"[错误] 清空队列失败: {e}")

def test_fifo():
    """
    测试 FIFO 功能
    """
    print("=== 测试 Redis 队列 FIFO 功能 ===")
    
    r = get_redis_client()
    if not r:
        return
    
    # 清空队列
    clear_queue(r)
    
    # 添加测试指令
    test_commands = [
        {"action": "take_off", "params": {"height": 1.0}},
        {"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}},
        {"action": "land"}
    ]
    
    print("\n1. 向队列添加指令...")
    for cmd in test_commands:
        add_to_queue(r, cmd)
        time.sleep(0.1)  # 确保时间戳不同
    
    # 显示队列状态
    print("\n2. 队列状态:")
    show_queue_status(r)
    
    # 读取并验证
    print("\n3. 从队列读取指令 (FIFO 顺序):")
    read_commands = []
    while True:
        data = read_from_queue(r)
        if not data:
            break
        read_commands.append(data['command'])
        print(f"   读取: {data['command']['action']}")
    
    # 验证顺序
    print("\n4. 验证 FIFO 顺序:")
    if read_commands == test_commands:
        print("[OK] FIFO 顺序正确！")
        print(f"   添加顺序: {[cmd['action'] for cmd in test_commands]}")
        print(f"   读取顺序: {[cmd['action'] for cmd in read_commands]}")
    else:
        print("[错误] FIFO 顺序不正确！")
        print(f"   添加顺序: {[cmd['action'] for cmd in test_commands]}")
        print(f"   读取顺序: {[cmd['action'] for cmd in read_commands]}")
    
    # 再次显示队列状态
    print("\n5. 最终队列状态:")
    show_queue_status(r)

def main():
    """
    主函数
    """
    print("=== Redis 队列测试 ===")
    
    # 运行 FIFO 测试
    test_fifo()
    
    # 测试与 b_test_script.py 的集成
    print("\n=== 测试与 b_test_script.py 集成 ===")
    print("1. 请运行: python b_test_script.py")
    print("2. 然后再次运行此脚本检查队列")

if __name__ == "__main__":
    try:
        import redis
        print("[OK] redis 模块已安装")
    except ImportError:
        print("[错误] redis 模块未安装！")
        print("请运行: pip install redis")
        exit(1)
    
    main()
