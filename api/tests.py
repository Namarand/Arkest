from django.test import TestCase
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test import Client

 def getToken(username, password = '12'):
    client = Client()
    response = client.post('/api-token-auth/', {"username":username,"password": password})
    return response.json()["token"]

class JwtTokenTest(TestCase):
    def setUp(self):
         User.objects.create_user(username='normal', password='12', email='')

    def test_get_jwt(self):
        self.assertEqual(400,400)
        client = Client()
        response = client.post('/api-token-auth/', {"username":'normal',"password":'12'})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()["token"]), 0)
        response = client.post('/api-token-auth/',)
        self.assertEqual(response.status_code, 400)

    def test_refresh_jwt(self):
        client = Client()
        response = client.post('/api-token-auth/', {"username":'normal',"password":'12'})
        response = client.post('/api-token-refresh/', {"token":response.json()["token"]})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()["token"]), 0)
        response = client.post('/api-token-refresh/', {"token":'MyawesomeJWT'})
        self.assertEqual(response.status_code, 400)

class PermissionTest(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='12', email='')
        user = User.objects.create_user(username='ApiUser', password='12', email='')
        viewer = User.objects.create_user(username='ApiViewer', password='12', email='')
        User.objects.create_user(username='normal', password='12', email='')
        my_group = Group.objects.get(name='ApiUser')
        my_group.user_set.add(user)
        my_group = Group.objects.get(name='ApiViewer')
        my_group.user_set.add(viewer)

    def test_get_dinosaur_list(self):
        client = Client()
        response = client.get('/dinosaurs/list/', **{"Authorization":'JWT ' + getToken("admin")})
        self.assertEqual(response.status_code, 200)
        response = client.get('/dinosaurs/list/', **{"Authorization":'JWT ' + getToken("ApiUser")})
        self.assertEqual(response.status_code, 200)
        response = client.get('/dinosaurs/list/', **{"Authorization":'JWT ' + getToken("ApiViewer")})
        self.assertEqual(response.status_code, 200)
        response = client.get('/dinosaurs/list/', **{"Authorization":'JWT ' + getToken("normal")})
        self.assertEqual(response.status_code, 401)
        response = client.get('/dinosaurs/list/', **{"Authorization":'JWT NotAGoodOne'})
        self.assertEqual(response.status_code, 401)
