from rest_framework import serializers
from api.models import Dinosaur, Parents


class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('id', 'race', 'name', 'owner', 'tribe', 'acquired', 'effectiveness',
                  'status', 'sexe', 'health', 'stamina', 'oxygen', 'food',
                  'weight', 'damage', 'speed', 'level')

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ('child', 'father', 'mother')
