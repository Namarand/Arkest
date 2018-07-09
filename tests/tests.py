import requests
import unittest


user="admin"
password="password123"

url = "http://127.0.0.1:8000/"
r = requests.post(url + "api-token-auth/", json={"username":user,"password":password})
jwt_token = r.json()["token"]

r = requests.get(url + "dinosaurs/list/", headers={"Authorization":'JWT ' + jwt_token})
print(r.json())
