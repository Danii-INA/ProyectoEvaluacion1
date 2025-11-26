from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_equipo, name='registrar_equipo'), 
    path('listado/', views.listado_equipos, name='listado_equipos'),    
    path('detalle/<str:nombre>/', views.detalle_equipo, name='detalle_equipo'), 
    path('eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
]