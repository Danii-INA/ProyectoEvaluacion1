from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from RecepcionApp.views import EquipoViewSet
from DiagnosticoApp.views import DiagnosticoViewSet
from EntregaApp.views import EntregaViewSet


router = DefaultRouter()
router.register(r'equipos', EquipoViewSet)
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'entregas', EntregaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', include('LoginApp.urls')),
    path('recepcion/', include('RecepcionApp.urls')),
    path('diagnostico/', include('DiagnosticoApp.urls')),
    path('entrega/', include('EntregaApp.urls')),


    path('api/', include(router.urls)),
]