from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantaViewSet, UsoMedicinalViewSet, RegiaoViewSet, FonteCientificaViewSet

router = DefaultRouter()
router.register(r'plantas', PlantaViewSet)
router.register(r'usos-medicinais', UsoMedicinalViewSet)
router.register(r'regioes', RegiaoViewSet)
router.register(r'fontes-cientificas', FonteCientificaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

