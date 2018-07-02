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
                        id INTEGER PRIMARY KEY,
                        race VARCHAR NOT NULL,
                        name VARCHAR NOT NULL,
                        owner VARCHAR NOT NULL,
                        tribe VARCHAR not null,
                        acquired VARCHAR not null,
                        effectiveness TINY INT CHECK (effectiveness >= 0 AND effectiveness <= 100),
                        status VARCHAR NOT NULL,
                        gender VARCHAR NOT NULL,
                        health TINY INT NOT NULL,
                        stamina TINY INT NOT NULL,
                        oxygen TINY INT NOT NULL,
                        food TINY INT NOT NULL,
                        weight TINY INT NOT NULL,
                        damage TINY INT NOT NULL,
                        speed TINY INT NOT NULL,
                        level TINY INT NOT NULL CHECK (level <= 71)
                    );"""
        parents = """CREATE TABLE IF NOT EXISTS parents (
                          id INTEGER,
                          father INTEGER,
                          mother INTEGER,
                          FOREIGN KEY(id) REFERENCES dinosaurs(id),
                          FOREIGN KEY(father) REFERENCES dinosaurs(id),
                          FOREIGN KEY(mother) REFERENCES dinosaurs(id)
                     );"""
        c = conn.cursor()
        c.execute(table)
        c.execute(parents)
        conn.commit()
        c.close()
        conn.close()
    except Error as e:
        print(e)

def add_dinosaur(conn, json):
    race = json["race"]
    name = json["name"]
    owner = json["owner"]
    tribe = json["tribe"]
    acquired = json["acquired"]
    effectiveness = json["effectiveness"]
    status = json["status"]
    gender = json["gender"]
    health = json["health"]
    stamina = json["stamina"]
    oxygen = json["oxygen"]
    food = json["food"]
    weight = json["weight"]
    damage = json["damage"]
    speed = json["speed"]
    level = json["level"]
    query = conn.execute("insert into dinosaurs values(\
        '{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}',\
        '{11}','{12}','{13}','{14}','{15}', '{16}');".format(race, name,\
        owner, trive, acquired, effectiveness, status, gender, health,\
        stamina, oxygen, food, weight, damage, speed, level))
    conn.commit()

def update_dinosaur(conn, ident, json):
    race = json["race"]
    name = json["name"]
    owner = json["owner"]
    tribe = json["tribe"]
    acquired = json["acquired"]
    effectiveness = json["effectiveness"]
    status = json["status"]
    gender = json["gender"]
    health = json["health"]
    stamina = json["stamina"]
    oxygen = json["oxygen"]
    food = json["food"]
    weight = json["weight"]
    damage = json["damage"]
    speed = json["speed"]
    level = json["level"]
    query = conn.execute("update dinosaurs set\
        race = '{0}', name = '{1}', owner = '{2}', tribe = '{3}',\
        acquired = '{4}', effectiveness = '{5}', status = '{6}',\
        gender = '{7}', health = '{8}', stamina = '{9}', oxygen = '{10}',\
        food = '{11}', weight = '{12}', damage = '{13}', speed = '{14}',\
        speed = '{15}', level = '{16}' where id = '{17}';".format(race, name,\
        owner, trive, acquired, effectiveness, status, gender, health,\
        stamina, oxygen, food, weight, damage, speed, level, ident))
    conn.commit()

def update_dinosaur_stat(conn, ident, field, json):
    value = json["value"]
    query = conn.execute("update dinosaurs set {0} = '{1}' where id = '{2}';"\
        .format(field, value, ident))
    conn.commit()
