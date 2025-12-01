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


# PLANTA

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    filterset_fields = [
        'nome_cientifico',
        'nome_popular',
        'risco_extincao',
        'regioes__tipo_bioma',
    ]
    
    ordering_fields = [
    'nome_cientifico',
    'nome_popular',
    'data_registro'
]

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


# USO MEDICINAL

class UsoMedicinalViewSet(viewsets.ModelViewSet):
    queryset = UsoMedicinal.objects.all()
    serializer_class = UsoMedicinalSerializer
    filterset_fields = ['parte_utilizada', 'indicacao']
    ordering_fields = ['parte_utilizada']


# REGIÃO

class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    filterset_fields = ['nome', 'tipo_bioma']
    ordering_fields = ['nome', 'tipo_bioma']


# FONTE CIENTÍFICA

class FonteCientificaViewSet(viewsets.ModelViewSet):
    queryset = FonteCientifica.objects.all()
    serializer_class = FonteCientificaSerializer
    filterset_fields = ['ano', 'fonte']
    ordering_fields = ['ano', 'titulo']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Planta, UsoMedicinal, Regiao, FonteCientifica


@api_view(['GET'])
def dashboard_geral(request):
    total_plantas = Planta.objects.count()
    total_extincao = Planta.objects.filter(risco_extincao=True).count()
    total_usos = UsoMedicinal.objects.count()
    total_regioes = Regiao.objects.count()
    total_fontes = FonteCientifica.objects.count()

    plantas_recentes = Planta.objects.order_by('-data_registro')[:5]

    return Response({
        "estatisticas": {
            "total_plantas": total_plantas,
            "total_em_risco_extincao": total_extincao,
            "total_usos_medicinais": total_usos,
            "total_regioes": total_regioes,
            "total_fontes_cientificas": total_fontes,
        },
        "plantas_recentes": [
            {
                "id": p.id,
                "nome_popular": p.nome_popular,
                "nome_cientifico": p.nome_cientifico,
                "data_registro": p.data_registro,
                "imagem": request.build_absolute_uri(p.imagem.url) if p.imagem else None,
            }
            for p in plantas_recentes
        ]
    })
