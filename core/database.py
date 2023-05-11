import psycopg2
from core.config import *

def PGconnection():
    with psycopg2.connect(
        host = PGHOST,
        database = PGDATABASE,
        user = PGUSER,
        password = PGPASSWORD,
        port = PGPORT) as connection:
        connection.autocommit = True
    return connection

def CheckRegister(user_id):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE userid = {user_id}")
        usercheck = cursor.fetchone
        return usercheck

def RegistrationUserPG(user_id, username, firstname, lastname, phone):
    with PGconnection().cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(\
                id SERIAL PRIMARY KEY,\
                userid BIGINT NOT NULL,\
                username VARCHAR(50) DEFAULT 'Not user_name',\
                first VARCHAR(250) DEFAULT 'Not first_name',\
                last VARCHAR(250) DEFAULT 'Not last_name',\
                phone VARCHAR(50) NOT NULL,\
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        if CheckRegister(user_id) is None:
            cursor.execute(
                "INSERT INTO users(userid, username, first, last, phone)\
                    VALUES (%s, %s, %s, %s, %s)", (user_id, username, firstname, lastname, phone)
            )
        else:
            pass