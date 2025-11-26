from rest_framework import viewsets
from .models import Planta, UsoMedicinal, Regiao
from .serializers import (
    PlantaSerializer,
    UsoMedicinalSerializer,
    RegiaoSerializer
)


class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer


class UsoMedicinalViewSet(viewsets.ModelViewSet):
    queryset = UsoMedicinal.objects.all()
    serializer_class = UsoMedicinalSerializer


class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
