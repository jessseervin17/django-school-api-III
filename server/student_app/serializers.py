from rest_framework import serializers
from .models import Student

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =[]