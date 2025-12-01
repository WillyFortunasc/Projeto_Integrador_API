from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlantaViewSet, UsoMedicinalViewSet,
    RegiaoViewSet, FonteCientificaViewSet,
    dashboard_geral
)

router = DefaultRouter()
router.register('plantas', PlantaViewSet)
router.register('usos-medicinais', UsoMedicinalViewSet)
router.register('regioes', RegiaoViewSet)
router.register('fontes-cientificas', FonteCientificaViewSet)

urlpatterns = [
    path('dashboard-geral/', dashboard_geral),
    path('', include(router.urls)),
]
