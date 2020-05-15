import redis
import pymongo
import json

def redisProxy():
    client = redis.Redis(host='localhost', port=6379)
    return client

def mongoProxy():
    client = pymongo.MongoClient("mongodb://localhost:27017", connect=False)
    database = client.get_database("datahub")
    return database.get_collection("instruments")

def read(order_book_id="000001.XSHE"):
    redis_client = redisProxy()
    mongo_client = mongoProxy()
    redis_cache = redis_client.get(order_book_id)
    # 如果缓存为空再去mongo拿数据, 否则直接返回
    if redis_cache is None:
        data = mongo_client.find_one({"order_book_id": order_book_id}, {"_id": 0})
        if not data:
            return
        redis_client.set(order_book_id, json.dumps(data))
        print("Read from mongo data")
        return data
    print("Read from redis cache")
    return json.loads(redis_cache)

def write(order_book_id="000001.XSHE"):
    redis_client = redisProxy()
    mongo_client = mongoProxy()
    try:
        mongo_client.update_one(
            {"order_book_id": order_book_id},
            {"$set": {"symbol": "建设银行", "status": "activate"}}
        )
        redis_client.delete(order_book_id)
        print("Delete redis cache")
    except Exception as identifier:
        print(str(identifier))
        return
    return "ok"
    


if "__main__" == __name__:
    read_data = read()
    print(read_data, type(read_data))
    write_data = write()
    print(write_data, type(write_data))
    read_data = read()
    print(read_data, type(read_data))