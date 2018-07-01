from database import *
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import *

app = Flask(__name__)
api = Api(app)

@app.route("/list", methods=["GET"])
def list():
    conn = create_connection("dabase.db") # connect to database
    query = conn.execute("select distinct race from dinosaurs")
    return jsonify({'races': [i[0] for i in query.fetchall()]})

@app.route("/new", methods=["POST"])
def new():
    conn = create_connection("dabase.db")
    print(request.get_json())
    race = request.json["race"]
    name = request.json["name"]
    level = request.json["level"]
    owner = request.json["owner"]
    tribe = request.json["tribe"]
    acquired = request.json["acquired"]
    effectiveness = request.json["effectiveness"]
    status = request.json["status"]
    gender = request.json["gender"]
    health = request.json["health"]
    stamina = request.json["stamina"]
    oxygen = request.json["oxygen"]
    food = request.json["food"]
    weight = request.json["weight"]
    damage = request.json["damage"]
    speed = request.json["speed"]
    query = conn.execute("insert into dinosaurs values(\
        '{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}',\
        '{11}','{12}','{13}','{14}','{15}','{16}')".format(race, name,\
        owner, trive, acquired, effectiveness, status, gender, health,\
        stamina, oxygen, food, weight, damage, speed))
    conn.commit()
    query = conn.execute("SELECT last_insert_rowid()")
    return jsonify({ "id" : query.fetchall()})

if __name__ == '__main__':
    conn = create_connection("dabase.db")
    if conn is not None:
        create_table(conn)
        app.run(port='5002')
