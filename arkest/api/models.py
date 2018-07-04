from django.db import models

# Create your models here.
class Dinosaur(models.Model):
    race = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=100, blank=True, default='')
    tribe = models.CharField(max_length=100, blank=True, default='')
    acquired = models.BooleanField(choices=((True, 'Tamed'), (False, 'Breeded')))
    effectiveness = models.CharField(max_length=100, blank=True, default='')
    status = models.BooleanField(choices=((True, 'Alive'), (False, 'Dead')))
    sexe = models.BooleanField(choices=((True, 'Male'), (False, 'Female')))
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
