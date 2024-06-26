from rest_framework import serializers
from fichas.models import Ficha

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'
