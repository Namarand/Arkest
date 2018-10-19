from rest_framework.test import APITestCase
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test import Client
from stats.models import *
from stats.serializers import *

def getToken(username, password = '12'):
    client = Client()
    response = client.post('/api-token-auth/', {"username":username,"password": password})
    return response.json()["token"]

class StatsManipulation(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))

    def test_create_dinosaur(self):
        body = {
            "race" : "Saber",
            "tbhm": 42,
            "health" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "stamina" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "oxygen" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "food" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "weight" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "meleeDamage" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "movementSpeed" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
            "torpidity" : {
                "base" : 1,
                "increaseWild" : 2,
                "increaseDomesticate" : 3,
                "tamingAddition" : 4,
                "tamingMultiplication" : 5,
            },
        }
        response = self.client.post('/stats/', body, format='json')
        print(response)
