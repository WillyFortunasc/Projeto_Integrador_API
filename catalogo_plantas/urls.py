from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantaViewSet, UsoMedicinalViewSet, RegiaoViewSet

router = DefaultRouter()
router.register(r'plantas', PlantaViewSet)
router.register(r'usos', UsoMedicinalViewSet)
router.register(r'regioes', RegiaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
