from database import *
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import *

app = Flask(__name__)
api = Api(app)

def check(json):
    if json["acquired"] != "tamed" OR json["acquired"] != "breeded":
        return "acquired must me 'tamed' or 'breeded'"
    if json["status"] != "alive" OR json["status"] != "dead":
        return "status must me 'alive' or 'dead'"
    if json["gender"] != "male" OR json["gender"] != "female":
        return "gender must me 'male' or 'female'"
    return None

@app.route("/list", methods=["GET"])
def list():
    conn = create_connection("dabase.db") # connect to database
    query = conn.execute("select distinct race from dinosaurs")
    return jsonify({'races': [i[0] for i in query.fetchall()]})

@app.route("/new", methods=["POST"])
def new():
    failure = check(request.json)
    if failure is not None:
        return jsonify({ "failure" : failure})
    conn = create_connection("dabase.db")
    add_dinosaur(conn, request.json)
    query = conn.execute("SELECT last_insert_rowid()")
    return jsonify({ "id" : query.fetchall()})

if __name__ == '__main__':
    conn = create_connection("dabase.db")
    if conn is not None:
        create_table(conn)
        app.run(port='5002')
