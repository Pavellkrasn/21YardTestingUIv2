from configuration.connector import create_connection
from configuration.sql_constants import *
import psycopg2


def confirm_user_email(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(CONFIRM_EMAIL_BY_USER_EMAIL, {'email': email})
        conn.commit()
    return

def confirm_user_phone(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(CONFIRM_PHONE_BY_USER_EMAIL, {'email': email})
        conn.commit()
    return


def is_user_email_confirmed(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(GET_USER_EMAIL_PHONE_CONFIRMED, {'email': email})
            result = cur.fetchone()
        except psycopg2.Error:
            conn.rollback()
            raise
    return result[0]


def is_user_phone_confirmed(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(GET_USER_EMAIL_PHONE_CONFIRMED, {'email': email})
            result = cur.fetchone()
        except psycopg2.Error:
            conn.rollback()
            raise
    return result[1]


def delete_applications(work_scope: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(DELETE_APPLICATIONS, {'work_scope': work_scope})
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            raise
    return

def delete_companies(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(DELETE_COMPANIES, {'email': email})
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            raise
    return

def update_applications_counter(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(UPDATE_APPLICATIONS_COUNTER, {'email': email})
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            raise

def get_user_id_by_email(email: str):
    conn = create_connection()
    with conn.cursor() as cur:
        try:
            cur.execute(GET_USER_BY_EMAIL, {'email': email})
            result = cur.fetchone()
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            raise
    return result[0]









