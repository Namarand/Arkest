from database import *
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import *

app = Flask(__name__)
api = Api(app)

class List(Resource):
    def get(self):
        conn = create_connection("dabase.db") # connect to database
        query = conn.execute("select race from dinosaurs")
        return {'race': query.fetchall()}


api.add_resource(List, '/list') # Route_1

if __name__ == '__main__':
    conn = create_connection("dabase.db")
    if conn is not None:
        create_table(conn)
        task = (1, "spino")
        sql = ''' INSERT INTO dinosaurs(id, race)
                      VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        print(cur.lastrowid)
        conn.commit()
        app.run(port='5002')
