import redis
from configuration.connector import pool

def delete_cache_by_key(key: str):
    client = redis.Redis(connection_pool=pool)
    client.delete(key)

