from postgres_configuration.connector import create_connection
from postgres_configuration.sql_constants import *


def confirm_user_email(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(CONFIRM_EMAIL_BY_USER_EMAIL, {'email':email})
        conn.commit()
    return

def confirm_user_phone(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(CONFIRM_PHONE_BY_USER_EMAIL, {'email':email})
        conn.commit()
    return

def is_user_email_confirmed(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(GET_USER_EMAIL_PHONE_CONFIRMED, {'email':email})
        result = cur.fetchone()
        print(result)
    return result[0]

def is_user_phone_confirmed(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(GET_USER_EMAIL_PHONE_CONFIRMED, {'email':email})
        result = cur.fetchone()
        print(result)
    return result[1]
