import redis
import pymongo
import json

def redisProxy():
    client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return client

def mongoProxy():
    client = pymongo.MongoClient("mongodb://localhost:27017", connect=False)
    database = client.get_database("datahub")
    return database.get_collection("abc")

# def read(order_book_id="000001.XSHE"):
#     redis_client = redisProxy()
#     mongo_client = mongoProxy()
#     redis_cache = redis_client.get(order_book_id)
#     # 如果缓存为空再去mongo拿数据, 否则直接返回
#     if redis_cache is None:
#         data = mongo_client.find_one({"order_book_id": order_book_id}, {"_id": 0})
#         if not data:
#             return
#         redis_client.set(order_book_id, json.dumps(data))
#         print("Read from mongo data")
#         return data
#     print("Read from redis cache")
#     return json.loads(redis_cache)

def read_proxy(mongo_proxy, redis_proxy, projection, filter_, cache_key, inside_key=None, cache_type="string", **kwargs):
    if "string" == cache_type:
        redis_cache = redis_proxy.get(cache_key)
        if redis_cache is None:
            sort = kwargs.get("sort")
            data = mongo_proxy.find_one(projection, filter_, sort=sort)
            if not data:
                return
            redis_proxy.set(cache_key, json.dumps(data))
            print("Read from mongo data: {}".format(data))
            return data
        print("Read from redis cache: {}".format(redis_cache))
        return json.loads(redis_cache)
    elif "hash" == cache_type:
        redis_cache = redis_proxy.hvals(cache_key)
        if redis_cache is None:
            sort = kwargs.get("sort")
            data = list(mongo_proxy.find(projection, filter_, sort=sort))
            if not data:
                return
            target = kwargs.get("target")
            for x in data:
                redis_proxy.hset(cache_key, {data[target]: json.dumps(data)})
            print("Read from mongo data")
            return data
        print("Read from redis cache")
        if inside_key is not None:
            return json.loads(redis_proxy.hget(cache_key, inside_key))
        else:
            return [json.loads(x) for x in redis_cache]


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

def write_proxy(mongo_proxy, redis_proxy, filter_, update, cache_key, inside_key=None, cache_type="string", **kwagrs):
    try:
        mongo_proxy.update_one(
            filter_,
            {"$set": update},
            upsert=True
        )

        if "string" == cache_type:
            redis_proxy.delete(cache_key)
        elif "hash" == cache_type:
            if inside_key is not None:
                redis_proxy.hdel(cache_key, inside_key)
            else:
                redis_proxy.delete(cache_key)
        print("Delete redis cache")
    except Exception as identifier:
        print(str(identifier))
        return
    return "ok"
    


if "__main__" == __name__:
    mongo_proxy = mongoProxy()
    redis_proxy = redisProxy()
    # write_res = write_proxy(
    #     mongo_proxy, redis_proxy, {"a": 1}, {"b": 11, "c": 12}, "doit"
    # )
    # print(write_res)

    read_res = read_proxy(
        mongo_proxy, redis_proxy, {"a": 1}, {"_id": 0}, "doit"
    )
    print(read_res, type(read_res))