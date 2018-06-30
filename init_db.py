import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None

def create_table(conn):
    try:
        table = """CREATE TABLE IF NOT EXISTS dinosaurs (
                        id UNSIGNED BIG INT PRIMARY KEY,
                        race VARCHAR NOT NULL,
                        name VARCHAR NOT NULL,
                        level SMALL INT NOT NULL,
                        owner VARCHAR NOT NULL,
                        tribe VARCHAR not null,
                        acquired VARCHAR not null,
                        effectiveness TINY INT,
                        status VARCHAR NOT NULL,
                        gender VARCHAR NOT NULL,
                        health TINY INT NOT NULL,
                        stamina TINY INT NOT NULL,
                        oxygen TINY INT NOT NULL,
                        food TINY INT NOT NULL,
                        weight TINY INT NOT NULL,
                        damage TINY INT NOT NULL,
                        speed TINY INT NOT NULL
                    );"""
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection("dabase.db")
    if conn is not None:
        create_table(conn)
