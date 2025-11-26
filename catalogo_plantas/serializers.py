from rest_framework import serializers
from .models import Planta, UsoMedicinal, Regiao


class UsoMedicinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoMedicinal
        fields = '__all__'


class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = '__all__'


class PlantaSerializer(serializers.ModelSerializer):
    usos_medicinais = UsoMedicinalSerializer(many=True, read_only=True)
    regioes = RegiaoSerializer(many=True, read_only=True)

    class Meta:
        model = Planta
        fields = '__all__'
