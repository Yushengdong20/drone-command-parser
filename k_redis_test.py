import redis
import json
import time

def test_redis_operations():
    """
    测试Redis存入和读取操作
    """
    print("=== Redis 操作测试 ===")
    
    try:
        # 尝试连接Redis
        print("1. 尝试连接Redis...")
        r = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        
        # 测试连接
        r.ping()
        print("✓ Redis连接成功！")
        
        # 测试存入数据
        print("\n2. 测试存入数据...")
        test_data = {
            "action": "take_off",
            "params": {
                "height": 1.0
            },
            "timestamp": time.time()
        }
        
        # 存入JSON数据
        r.set("drone_command", json.dumps(test_data))
        print("✓ 数据存入成功！")
        print(f"  存入的数据: {test_data}")
        
        # 测试读取数据
        print("\n3. 测试读取数据...")
        retrieved_data = r.get("drone_command")
        if retrieved_data:
            retrieved_data = json.loads(retrieved_data)
            print("✓ 数据读取成功！")
            print(f"  读取的数据: {retrieved_data}")
        else:
            print("✗ 读取数据失败")
        
        # 测试删除数据
        print("\n4. 测试删除数据...")
        r.delete("drone_command")
        print("✓ 数据删除成功！")
        
        # 验证删除
        deleted_check = r.get("drone_command")
        if deleted_check is None:
            print("✓ 数据已确认删除")
        else:
            print("✗ 数据删除失败")
        
        print("\n=== Redis 操作测试完成 ===")
        
    except redis.ConnectionError:
        print("\n✗ Redis连接失败！")
        print("  原因: Redis服务器未运行或未安装")
        print("  请按照以下步骤安装和启动Redis:")
        print("  1. 下载Redis: https://redis.io/download")
        print("  2. 安装Redis并启动服务")
        print("  3. 确保Redis服务在localhost:6379运行")
        
    except redis.RedisError as e:
        print(f"\n✗ Redis操作失败: {e}")
    
    except Exception as e:
        print(f"\n✗ 未知错误: {e}")

def test_redis_batch_operations():
    """
    测试Redis批量操作
    """
    print("\n=== Redis 批量操作测试 ===")
    
    try:
        r = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        
        r.ping()
        
        # 批量存入数据
        print("1. 批量存入数据...")
        batch_data = {
            "command1": json.dumps({"action": "take_off", "params": {"height": 1.0}}),
            "command2": json.dumps({"action": "land"}),
            "command3": json.dumps({"action": "direction_move", "params": {"orientation": "forward", "distance": 2.0}})
        }
        
        r.mset(batch_data)
        print("✓ 批量存入成功！")
        
        # 批量读取数据
        print("\n2. 批量读取数据...")
        keys = ["command1", "command2", "command3"]
        values = r.mget(keys)
        
        for key, value in zip(keys, values):
            if value:
                value = json.loads(value)
                print(f"  {key}: {value}")
            else:
                print(f"  {key}: 无数据")
        
        # 批量删除数据
        print("\n3. 批量删除数据...")
        r.delete(*keys)
        print("✓ 批量删除成功！")
        
        # 验证删除
        remaining = r.mget(keys)
        if all(v is None for v in remaining):
            print("✓ 所有数据已确认删除")
        else:
            print("✗ 部分数据删除失败")
        
        print("\n=== Redis 批量操作测试完成 ===")
        
    except redis.ConnectionError:
        print("\n✗ Redis连接失败！")
    except Exception as e:
        print(f"\n✗ 错误: {e}")

if __name__ == "__main__":
    # 检查是否安装了redis模块
    try:
        import redis
        print("✓ redis模块已安装")
    except ImportError:
        print("✗ redis模块未安装！")
        print("  请运行: pip install redis")
        exit(1)
    
    # 运行测试
    test_redis_operations()
    test_redis_batch_operations()
