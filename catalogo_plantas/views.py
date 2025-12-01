from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=True, methods=['get'], url_path='dashboard')
    def dashboard(self, request, pk=None):
        planta = self.get_object()

        usos = planta.usos_medicinais.all()
        regioes = planta.regioes.all()
        fontes = planta.fontes_cientificas.all()

        return Response({
            "id": planta.id,
            "nome_cientifico": planta.nome_cientifico,
            "nome_popular": planta.nome_popular,
            "descricao": planta.descricao,
            "imagem": request.build_absolute_uri(planta.imagem.url) if planta.imagem else None,
            "risco_extincao": planta.risco_extincao,
            "data_registro": planta.data_registro,

            "usos_medicinais": [
                {
                    "id": uso.id,
                    "parte_utilizada": uso.parte_utilizada,
                    "modo_preparo": uso.modo_preparo,
                    "indicacao": uso.indicacao
                } for uso in usos
            ],

            "regioes": [
                {
                    "id": reg.id,
                    "nome": reg.nome,
                    "bioma": reg.tipo_bioma  
                } for reg in regioes
            ],

            "fontes_cientificas": [
                {
                    "id": f.id,
                    "titulo": f.titulo,
                    "autores": f.autores,
                    "ano": f.ano,
                    "fonte": f.fonte,
                    "link": f.link,
                    "observacoes": f.observacoes
                } for f in fontes
            ]
        })


class UsoMedicinalViewSet(viewsets.ModelViewSet):
    queryset = UsoMedicinal.objects.all()
    serializer_class = UsoMedicinalSerializer


class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer


class FonteCientificaViewSet(viewsets.ModelViewSet):
    queryset = FonteCientifica.objects.all()
    serializer_class = FonteCientificaSerializer
