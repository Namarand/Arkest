from django.db import models

class StatDetail(models.Model):
    base = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)
    increaseWild = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)
    increaseDomesticate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)
    tamingAddition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)
    tamingMultiplication = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)

class RaceStats(models.Model):
    race = models.CharField(max_length=100, primary_key=True)
    tbhm = models.DecimalField(max_digits=12, decimal_places=4, blank=True, default=0)
    health = models.OneToOneField(StatDetail, related_name='health', on_delete=models.CASCADE)
    stamina = models.OneToOneField(StatDetail, related_name='stamina', on_delete=models.CASCADE)
    oxygen = models.OneToOneField(StatDetail, related_name='oxygen', on_delete=models.CASCADE)
    food = models.OneToOneField(StatDetail, related_name='food', on_delete=models.CASCADE)
    weight = models.OneToOneField(StatDetail, related_name='weight', on_delete=models.CASCADE)
    meleeDamage = models.OneToOneField(StatDetail, related_name='meleeDamage', on_delete=models.CASCADE)
    movementSpeed = models.OneToOneField(StatDetail, related_name='movementSpeed', on_delete=models.CASCADE)
    torpidity = models.OneToOneField(StatDetail, related_name='torpidity', on_delete=models.CASCADE)
