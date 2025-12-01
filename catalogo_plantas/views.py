from rest_framework import viewsets
from .models import Planta, UsoMedicinal, Regiao, FonteCientifica
from .serializers import (
    PlantaSerializer,
    UsoMedicinalSerializer,
    RegiaoSerializer,
    FonteCientificaSerializer
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


class FonteCientificaViewSet(viewsets.ModelViewSet):
    queryset = FonteCientifica.objects.all()
    serializer_class = FonteCientificaSerializer

