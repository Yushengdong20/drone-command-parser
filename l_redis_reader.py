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

def main():
    """
    主函数
    """
    print("=== Redis 指令读取工具 ===")
    print("从 Redis 队列中读取指令 (FIFO 顺序)")
    
    r = get_redis_client()
    if not r:
        return
    
    # 显示队列初始状态
    print("\n1. 初始队列状态:")
    show_queue_status(r)
    
    # 读取并处理指令
    print("\n2. 读取指令 (FIFO 顺序):")
    read_commands = []
    while True:
        data = read_from_queue(r)
        if not data:
            print("[信息] 队列为空，读取完成")
            break
        
        command = data['command']
        read_commands.append(command)
        
        print(f"\n读取指令:")
        print(f"  动作: {command['action']}")
        if 'params' in command:
            print(f"  参数: {json.dumps(command['params'], indent=2)}")
        print(f"  时间戳: {data['timestamp']}")
        
        # 模拟处理时间
        print("  处理中...")
        time.sleep(1)
        print("  处理完成")
    
    # 显示读取结果
    print("\n3. 读取结果:")
    print(f"   共读取 {len(read_commands)} 条指令")
    if read_commands:
        print("   读取顺序:")
        for i, cmd in enumerate(read_commands, 1):
            print(f"     {i}. {cmd['action']}")
    
    # 显示最终队列状态
    print("\n4. 最终队列状态:")
    show_queue_status(r)
    
    print("\n=== 操作完成 ===")
    print("请运行 k_redis_writer.py 添加新的指令到队列")

if __name__ == "__main__":
    try:
        import redis
        print("[OK] redis 模块已安装")
    except ImportError:
        print("[错误] redis 模块未安装！")
        print("请运行: pip install redis")
        exit(1)
    
    main()
