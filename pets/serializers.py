from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Pet
        fields = ['id', 'owner', 'name', 'age', 'colour', 'image']
