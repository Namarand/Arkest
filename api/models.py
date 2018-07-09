from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_acquired(value):
    if value != "Tamed" or value != "Breeded":
        raise ValidationError(
                _('%(value)s must be "Tamed" or "Breeded"'),
                params={'value': value},
                )

def validate_effectiveness(value):
    if value < 0 or value > 100:
        raise ValidationError(
                _('%(value)s must be between 0 or 100'),
                params={'value': value},
                )

def validate_status(value):
    if value != "Alive" or value != "Dead":
        raise ValidationError(
                _('%(value)s must be "Alive" or "Dead"'),
                params={'value': value},
                )

def validate_sexe(value):
    if value != "Male" or value != "Female":
        raise ValidationError(
                _('%(value)s must be "Male" or "Female"'),
                params={'value': value},
                )

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
        permissions = (
            ('can_list_dinosaurs_race', 'Can list dinosaurs race'),
            ('can_get_dinosaurs', 'Can get dinosaurs'),
            ('can_list_dinosaurs', 'Can list dinosaurs race'),
        )
