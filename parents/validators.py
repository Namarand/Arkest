from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from api.models import Dinosaur

def validate_father(value):
    if Dinosaur.objects.get(pk=value).sexe != "Male":
        raise ValidationError(
                _('father must be a male'),
                params={'value': value},
                )

def validate_mother(value):
    if Dinosaur.objects.get(pk=value).sexe != "Female":
        raise ValidationError(
                _('mother must be a female'),
                params={'value': value},
                )
