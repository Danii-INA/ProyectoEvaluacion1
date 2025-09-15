# EntregaApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_entrega, name='verificar_entrega'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    # La URL ahora acepta un nombre de cliente
    path('comprobante/<str:cliente>/', views.comprobante_entrega, name='comprobante_entrega'),
]