import psycopg2
from core.config import *
from random import randint

def PGconnection():
    with psycopg2.connect(
        host = PGHOST,
        database = PGDATABASE,
        user = PGUSER,
        password = PGPASSWORD,
        port = PGPORT ) as connetion:
        connetion.autocommit = True
    return connetion


def CheckRegister(user_id):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE userid = {user_id}")
        usercheck = cursor.fetchone()
        return usercheck


def RegistrationUserPG(user_id, username, firstname, lastname, phone):
    with PGconnection().cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(\
                id SERIAL PRIMARY KEY,\
                userid BIGINT NOT NULL,\
                username VARCHAR(50) DEFAULT 'Not username',\
                first_name VARCHAR(250) DEFAULT 'Not first_name',\
                last_name VARCHAR(250) DEFAULT 'Not last_name',\
                phone VARCHAR(50) NOT NULL,\
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        if CheckRegister(user_id) is None:
            cursor.execute(
                "INSERT INTO users(userid, username, first_name, last_name, phone)\
                    VALUES(%s, %s, %s, %s, %s)", (user_id, username, firstname, lastname, phone)
            )
        else:
            pass
    

def add_information_places(category, title, info, url, photo):
    with PGconnection().cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS places(\
                id SERIAL PRIMARY KEY,\
                category VARCHAR(150) NOT NULL,\
                title VARCHAR(150) NOT NULL,\
                information VARCHAR(255) NOT NULL,\
                url TEXT NOT NULL,\
                photo TEXT NOT NULL,\
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            )
        cursor.execute(
            f"SELECT * FROM places WHERE title = '{title}'\
                and information = '{info}' and url = '{url}'"
        )
        CheckPlaces = cursor.fetchone()
        if CheckPlaces is None:
            cursor.execute(
            "INSERT INTO places (category, title, information, url, photo)\
                VALUES (%s, %s, %s, %s, %s)", (category, title, info, url, photo)
            )
        else:
            pass

def get_location():
    with PGconnection().cursor() as cursor:
        data = []
        for i in range(1, 6):
            cursor.execute(
                f"SELECT title FROM places WHERE id = {randint(1, 1638)}"
            )
            one_location = cursor.fetchone()
            data.append(one_location)
    
    return data


def get_category_location(category):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM places WHERE category = '{category}'")
        all_location = cursor.fetchall()
    return all_location


def get_name_location(title):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM places WHERE title = '{title}'")
        info_location = cursor.fetchone()

    return info_location