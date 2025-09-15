# SistemaGestion/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # Importa la vista de redirección

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Cuando alguien visite la raíz (''), se redirige automaticamente a '/login/'.
    path('', RedirectView.as_view(url='/login/', permanent=True)),

    # 2. Cuando alguien visite '/login/', usa el mapa de la LoginApp.
    path('login/', include('LoginApp.urls')),

    # Rutas para las otras apps
    path('recepcion/', include('RecepcionApp.urls')),
    path('diagnostico/', include('DiagnosticoApp.urls')),
    path('entrega/', include('EntregaApp.urls')),
]