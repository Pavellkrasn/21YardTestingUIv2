from typing import Optional

import psycopg2
from psycopg2._psycopg import connection

from settings import settings

_connection: Optional[connection] = None


def create_connection():
    global _connection
    if not _connection or _connection.closed:
        _connection = psycopg2.connect(dbname=settings.POSTGRES_DB, user=settings.POSTGRES_USER,
                                       password=settings.POSTGRES_PASSWORD, host=settings.POSTGRES_HOST,
                                       port=settings.POSTGRES_PORT)
    return _connection
