from django.db import models
from api.models import Dinosaur
from parents.validators import *


# Create your models here.
class Parents(models.Model):
    child = models.ForeignKey(Dinosaur, on_delete=models.CASCADE, related_name='child')
    father = models.ForeignKey(Dinosaur, on_delete=models.SET_NULL, null=True, related_name='father')#, validators=[validate_father])
    mother = models.ForeignKey(Dinosaur, on_delete=models.SET_NULL, null=True, related_name='mother')#, validators=[validate_mother])

    class Meta:
        ordering = ('child',)
