from rest_framework.test import APITestCase
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test import Client
from api.models import Dinosaur
from api.serializers import DinosaurSerializer

def getToken(username, password = '12'):
    client = Client()
    response = client.post('/api-token-auth/', {"username":username,"password": password})
    return response.json()["token"]


class JwtTokenTest(APITestCase):
    def setUp(self):
         User.objects.create_user(username='normal', password='12', email='')

    def test_get_jwt(self):
        response = self.client.post('/api-token-auth/', {"username":'normal',"password":'12'})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()["token"]), 0)
        response = self.client.post('/api-token-auth/',)
        self.assertEqual(response.status_code, 400)

    def test_refresh_jwt(self):
        response = self.client.post('/api-token-auth/', {"username":'normal',"password":'12'})
        response = self.client.post('/api-token-refresh/', {"token":response.json()["token"]})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()["token"]), 0)
        response = self.client.post('/api-token-refresh/', {"token":'MyawesomeJWT'})
        self.assertEqual(response.status_code, 400)

class PermissionTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        user = User.objects.create_user(username='ApiUser', password='12', email='')
        viewer = User.objects.create_user(username='ApiViewer', password='12', email='')
        User.objects.create_user(username='normal', password='12', email='')
        my_group = Group.objects.get(name='ApiUser')
        my_group.user_set.add(user)
        my_group.save()
        my_group = Group.objects.get(name='ApiViewer')
        my_group.user_set.add(viewer)
        my_group.save()

    def TestAccessGet(self, path, return_value = 200):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))
        response = self.client.get(path)
        self.assertEqual(response.status_code, return_value)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('ApiUser'))
        response = self.client.get(path)
        self.assertEqual(response.status_code, return_value)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('ApiViewer'))
        response = self.client.get(path)
        self.assertEqual(response.status_code, return_value)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('normal'))
        response = self.client.get(path)
        self.assertEqual(response.status_code, 403)
        response = self.client.get(path)
        self.assertEqual(response.status_code, 403)

    def test_get_dinosaur_list(self):
        self.TestAccessGet(path='/dinosaurs/list/')

    def test_get_dinosaur_race(self):
        self.TestAccessGet(path='/dinosaurs/list/etc/', return_value=404)

    def test_get_dinosaurs(self):
        self.TestAccessGet(path='/dinosaurs/0/', return_value=404)

    def test_post_dinosaurs(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))
        response = self.client.post('/dinosaurs/', {}, format='json')
        self.assertEqual(response.status_code, 201)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('ApiUser'))
        response = self.client.post('/dinosaurs/', {}, format='json')
        self.assertEqual(response.status_code, 201)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('ApiViewer'))
        response = self.client.post('/dinosaurs/', {}, format='json')
        self.assertEqual(response.status_code, 403)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('normal'))
        response = self.client.post('/dinosaurs/', {}, format='json')
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/dinosaurs/', {}, format='json')
        self.assertEqual(response.status_code, 403)


class DinosaurListComportement(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        dino = Dinosaur(race="Sabertooth")
        dino.save()
        dino = Dinosaur(race="Rex")
        dino.save()
        dino = Dinosaur(race="Sabertooth")
        dino.save()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))

    def getList(self, extend=""):
        return self.client.get('/dinosaurs/list/' + extend)

    def test_dinosaur_list(self):
        result = self.getList().json()
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["races"], ['Rex', 'Sabertooth'])

    def test_dinosaur_list_race(self):
        result = self.getList("Rex/").json()
        self.assertEqual(result["count"], 1)
        for rex in result["dinosaurs"]:
            self.assertEqual(rex["race"], "Rex")
        result = self.getList("Sabertooth/").json()
        self.assertEqual(result["count"], 2)
        for saber in result["dinosaurs"]:
            self.assertEqual(saber["race"], "Sabertooth")

    def test_dinosaur_list_race_non_existent(self):
        result = self.getList("ABCD/")
        self.assertEqual(result.status_code, 404)

class DinosaurManipulation(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        dino = Dinosaur(race="Sabertooth")
        dino.save()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + getToken('admin'))

    def test_create_dinosaur(self):
        body = {
            "name" : "test_name",
            "owner": "test_owner",
            "tribe": "test_tribe",
            "race": "Sabertooth",
            "acquired": "Breeded",
            "effectiveness": 100,
            "status": "Alive",
            "sexe": "Male",
            "health": 1,
            "stamina": 1,
            "oxygen": 1,
            "food": 1,
            "weight": 1,
            "damage": 1,
            "speed": 1,
            "level": 1,
        }
        response = self.client.post('/dinosaurs/', body, format='json')
        body["id"] = response.json()["id"]
        self.assertEqual(response.json(), body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(DinosaurSerializer(Dinosaur.objects.get(pk=body["id"])).data, body)

    def test_update_dinosaur(self):
        body = {
            "name" : "new_name"
        }
        response = self.client.put('/dinosaurs/1/', body, format='json')
        dino = Dinosaur.objects.get(pk=1)
        self.assertEqual(dino.name, "new_name")
        self.assertEqual(response.status_code, 200)

    def test_delete_dinosaur(self):
        response = self.client.delete('/dinosaurs/1/', {}, format='json')
        self.assertEqual(len(Dinosaur.objects.all()), 0)
