# DiagnosticoApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('asignar/', views.asignar_tecnico, name='asignar_tecnico'),
    path('evaluar/', views.evaluar_equipo, name='evaluar_equipo'),
    path('listado/', views.listado_diagnosticos, name='listado_diagnosticos'),
]