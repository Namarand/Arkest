from django.db import models
from api.models import Dinosaur
from parents.validators import *


# Create your models here.
class Parents(models.Model):
    child_id = models.ForeignKey(Dinosaur, on_delete=models.CASCADE, related_name='child_id')
    father_id = models.ForeignKey(Dinosaur, on_delete=models.SET_NULL, null=True, related_name='father_id', validators=[validate_father])
    mother_id = models.ForeignKey(Dinosaur, on_delete=models.SET_NULL, null=True, related_name='mother_id', validators=[validate_mother])

    class Meta:
        ordering = ('child_id',)
