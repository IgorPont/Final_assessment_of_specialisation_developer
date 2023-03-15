from getpass import getpass
from mysql.connector import *


def create_connection():
    """Подключиться к серверу mysql"""
    try:
        with connect(
                host="localhost",
                user=input("User name MySQL server: "),
                password=getpass("Enter password: "),
        ) as connection:
            print(connection)
    except Error as e:
        print(e)


def show_database():
    """Показать существующие базы данных"""
    try:
        with connect(
                host="localhost",
                user=input("User name MySQL server: "),
                password=getpass("Password: "),
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)


def create_connection_db(name_db):
    """Подключиться к существующей базе данных"""
    try:
        with connect(
                host="localhost",
                user=input("User name MySQL server: "),
                password=getpass("Password: "),
                database=name_db,
        ) as connection:
            print(connection)
    except Error as e:
        print(e)


def create_database_Human_friends():
    """Создать базу данных Human_friends"""
    try:
        with connect(
                host="localhost",
                user=input("User name MySQL server: "),
                password=getpass("Password: "),
        ) as connection:
            create_db_query = "CREATE DATABASE Human_friends"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)


def create_table(query):
    """Создать таблицу"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()



