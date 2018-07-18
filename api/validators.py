from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_acquired(value):
    if value != "Tamed" and value != "Breeded":
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
    if value != "Alive" and value != "Dead":
        raise ValidationError(
                _('%(value)s must be "Alive" or "Dead"'),
                params={'value': value},
                )

def validate_sexe(value):
    if value != "Male" and value != "Female":
        raise ValidationError(
                _('%(value)s must be "Male" or "Female"'),
                params={'value': value},
                )
