from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# 🔹 Rota raiz para evitar "Not Found"
def home(request):
    return JsonResponse({
        "status": "API online",
        "endpoints": {
            "admin": "/admin/",
            "token": "/api/token/",
            "token refresh": "/api/token/refresh/",
            "api base": "/api/",
            "catalogo plantas": "/api/catalogo/",
            "swagger": "/api/docs/swagger/",
            "redoc": "/api/docs/redoc/"
        }
    })


urlpatterns = [
    # Rota raiz
    path('', home),

    # Admin
    path('admin/', admin.site.urls),

    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # APIs
    path('api/', include('api.urls')),
    path('api/catalogo/', include('catalogo_plantas.urls')),

    # Documentação
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/docs/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]

# Arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
