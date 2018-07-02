from database import *
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import *

app = Flask(__name__)
api = Api(app)

def check(json):
    if json["acquired"] != "tamed" or json["acquired"] != "breeded":
        return "acquired must me 'tamed' or 'breeded'"
    if json["status"] != "alive" or json["status"] != "dead":
        return "status must me 'alive' or 'dead'"
    if json["gender"] != "male" or json["gender"] != "female":
        return "gender must me 'male' or 'female'"
    if json["health"] + json["stamina"] + json["food"] + json["oxygen"] +\
       json["weight"] + json["damage"] + json["speed"] > 450:
        return "dinosaurs level can't be above 450"
    return None

@app.route("/list", methods=["GET"])
def list():
    conn = create_connection("dabase.db") # connect to database
    query = conn.execute("select distinct race from dinosaurs")
    return jsonify({'races': [i[0] for i in query.fetchall()]})

@app.route("/list/<kind>", methods=["GET"])
def dinosaurs_get(kind):
    conn = create_connection("dabase.db")
    query = conn.execute("select * from dinosaurs where dinosaurs.race = '{0}'".format(kind))
    return jsonify ({'dinosaurs': query.fetchall()})

@app.route("/dinosaurs/<ident>", methods=["GET"])
def dinosaurs_get_by_id(ident):
    conn = create_connection("dabase.db")
    query = conn.execute("select * from dinosaurs where dinosaurs.id = '{0}'".format(ident))
    res = query.fetchone()
    if res is None:
        return jsonify({'failure': "no such id"})
    else:
        return jsonify ({res})

@app.route("/new", methods=["POST"])
def new():
    try:
        failure = check(request.json)
        if failure is not None:
            return jsonify({ "failure" : failure})
        if request.json is None:
            return jsonify({ "error": "missing body"})
        conn = create_connection("dabase.db")
        add_dinosaur(conn, request.json)
        query = conn.execute("SELECT last_insert_rowid()")
        return jsonify({ "id" : query.fetchall()})
    except sqlite3.IntegrityError as r:
        return jsonify({ "error" : "invalid value".format(\
           request.json["value"], field)})
    except Exception as r:
        print(r)
        return jsonify({ "error" : "internal error"})

@app.route("/update/dinosaurs/full/<ident>", methods=["POST"])
def dinosaurs_update(ident):
    try:
        if request.json is None:
            return jsonify({ "error": "missing body"})
        conn = create_connection("dabase.db")
        update_dinosaur(conn, ident, request.json)
        return jsonify({ "result" : "update succeed" })
    except sqlite3.IntegrityError as r:
        return jsonify({ "error" : "invalid value".format(\
           request.json["value"], field)})
    except Exception as r:
        print(r)
        return jsonify({ "error" : "internal error"})

@app.route("/update/dinosaurs/field/<ident>/<field>", methods=["POST"])
def dinosaurs_update_field(ident, field):
    try:
        if request.json is None:
            return jsonify({ "error": "missing body"})
        conn = create_connection("dabase.db")
        update_dinosaur_stat(conn, ident, field, request.json)
        return jsonify({ "result" : "update succeed" })
    except sqlite3.IntegrityError as r:
        return jsonify({ "error" : "{0} is not a valid value for {1}".format(\
           request.json["value"], field)})
    except Exception as r:
        print(r)
        return jsonify({ "error" : "internal error"})

@app.route("/delete/dinosaurs/<ident>", methods=["GET"])
def dinosaurs_remove(ident):
    conn = create_connection("dabase.db")
    remove_dinosaur(conn, ident)
    return jsonify({"result":"succesfully delete"})

if __name__ == '__main__':
    conn = create_connection("dabase.db")
    if conn is not None:
        create_table(conn)
        app.run(port='5002')
