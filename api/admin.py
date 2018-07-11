from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from api.models import Dinosaur

Group.objects.get_or_create(name="ApiUser")
Group.objects.get_or_create(name="ApiViewer")
admin.site.register(Dinosaur)
