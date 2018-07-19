from rest_framework import serializers
from parents.models import Parents


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ('child', 'father', 'mother')
