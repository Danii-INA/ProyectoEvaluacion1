# RecepcionApp/views.py
from django.shortcuts import render, redirect
from .models import Equipo

def registrar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    mensaje_exito = None
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        tipo_equipo = request.POST.get('tipo_equipo')
        problema = request.POST.get('problema')
        
        nuevo_equipo = Equipo(
            cliente=cliente,
            tipo_equipo=tipo_equipo,
            problema=problema
        )
        nuevo_equipo.save()
     
        return redirect(f"/diagnostico/asignar/?equipo_cliente={cliente}")

    return render(request, 'RecepcionApp/registrar_equipo.html')

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    
    todos_los_equipos = Equipo.objects.all()
    contexto = {'equipos': todos_los_equipos}
    return render(request, 'RecepcionApp/listado_equipos.html', contexto)

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('login')
    try:
        equipo_encontrado = Equipo.objects.get(cliente__iexact=nombre)
    except Equipo.DoesNotExist:
        equipo_encontrado = None
    return render(request, 'RecepcionApp/detalle_equipo.html', {'equipo': equipo_encontrado})

from rest_framework import viewsets
from .serializers import EquipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer