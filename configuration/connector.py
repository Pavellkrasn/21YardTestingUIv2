from typing import Optional

import redis

import psycopg2
from psycopg2._psycopg import connection

from settings import settings

_postgres_connection: Optional[connection] = None

def create_connection():
    global _postgres_connection
    if not _postgres_connection or _postgres_connection.closed:
        _postgres_connection = psycopg2.connect(dbname=settings.POSTGRES_DB, user=settings.POSTGRES_USER,
                                                password=settings.POSTGRES_PASSWORD, host=settings.POSTGRES_HOST,
                                                port=settings.POSTGRES_PORT)
    return _postgres_connection



REDIS_URL = f'redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}'
pool = redis.ConnectionPool.from_url(REDIS_URL, max_connections=10)



