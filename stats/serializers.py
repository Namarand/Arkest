from rest_framework import serializers
from stats.models import StatDetail, RaceStats

class StatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatDetail
        fields = ('base', 'increaseWild', 'increaseDomesticate', 'tamingAddition', 'tamingMultiplication',)

class RaceStatsSerializer(serializers.ModelSerializer):
    health = StatDetailSerializer(required=True)
    stamina = StatDetailSerializer(required=True)
    oxygen = StatDetailSerializer(required=True)
    food = StatDetailSerializer(required=True)
    weight = StatDetailSerializer(required=True)
    meleeDamage = StatDetailSerializer(required=True)
    movementSpeed = StatDetailSerializer(required=True)
    torpidity = StatDetailSerializer(required=True)
    class Meta:
        model = RaceStats
        fields = ('race', 'tbhm', 'health', 'stamina', 'oxygen', 'food',
                  'weight', 'meleeDamage', 'movementSpeed', 'torpidity',)
