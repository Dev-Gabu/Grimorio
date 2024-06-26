from rest_framework import serializers
from bestiario.models import Criatura

class CriaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criatura
        fields = '__all__'
