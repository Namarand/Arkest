from django.db.models import signals
from django.contrib.auth.models import Group, Permission

Group.objects.get_or_create(name="ApiUser")

#group = Group.objects.get(name="ApiUser")
