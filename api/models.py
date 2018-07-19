from django.db import models
from api.validators import *


# Create your models here.
class Dinosaur(models.Model):
    race = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=100, blank=True, default='')
    tribe = models.CharField(max_length=100, blank=True, default='')
    acquired = models.CharField(max_length=8, default='Tamed', validators=[validate_acquired])
    effectiveness = models.IntegerField(default=0, validators=[validate_effectiveness])
    status = models.CharField(max_length=6, default="Alive", validators=[validate_status])
    sexe = models.CharField(max_length=7, default="Male", validators=[validate_sexe])
    health = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    oxygen = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    class Meta:
        ordering = ('race',)
