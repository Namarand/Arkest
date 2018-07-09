from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from api.models import Dinosaur

group, other = Group.objects.get_or_create(name="ApiUser")

content_type = ContentType.objects.get_for_model(model=Dinosaur)
#get all permssions for this model
perms = Permission.objects.filter(content_type=content_type)

for p in perms:
    group.permissions.add(p)
#group = Group.objects.get(name="ApiUser")
