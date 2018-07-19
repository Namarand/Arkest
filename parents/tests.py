from rest_framework.test import APITestCase
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test import Client
from api.models import Dinosaur
from parents.models import Parents
from parents.serializers import ParentsSerializer

def getToken(username, password = '12'):
    client = Client()
    response = client.post('/api-token-auth/', {"username":username,"password": password})
    return response.json()["token"]

class ParentsTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        dino = Dinosaur(race="Sabertooth")
        dino.save()
        dino = Dinosaur(race="Sabertooth", sexe="Male")
        dino.save()
        dino = Dinosaur(race="Sabertooth", sexe="Female")
        dino.save()
        dino = Dinosaur(race="Sabertooth", sexe="Male")
        dino.save()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))

    def test_create_parents(self):
        body = {
            "child" : 1,
            "father" : 2,
            "mother" : 3
        }
        response = self.client.post('/parents/', body, format='json')
        self.assertEqual(ParentsSerializer(Parents.objects.get(pk=body["child"])).data, body)
        self.assertEqual(response.status_code, 200)

    def test_update_parents(self):
        parent = Parents(child=1, father=2, mother=3)
        parent.save()
        response = self.client.put('/parents/1', {"father":4}, format='json')
        self.assertEqual(Parents.objects.get(pk=1).father, 4)
        self.assertEqual(response.status_code, 201)
