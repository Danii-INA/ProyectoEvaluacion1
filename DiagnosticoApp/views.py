# DiagnosticoApp/views.py
from django.shortcuts import render, redirect
from RecepcionApp.models import Equipo 
from .models import Diagnostico      

def asignar_tecnico(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    equipos_pendientes = Equipo.objects.filter(estado='Recibido')
    contexto = { 'equipos': equipos_pendientes }
    return render(request, 'DiagnosticoApp/asignar_tecnico.html', contexto)


def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    if request.method == 'POST':
        equipo_id = request.POST.get('equipo_id')
        estudiante = request.POST.get('estudiante')
        diagnostico_txt = request.POST.get('diagnostico')
        solucion_txt = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        
        try:
            equipo_obj = Equipo.objects.get(id=equipo_id)
            
            nuevo_diagnostico = Diagnostico(
                equipo=equipo_obj,
                estudiante=estudiante,
                diagnostico_problema=diagnostico_txt,
                solucion=solucion_txt,
                tipo_solucion=tipo_solucion
            )
            nuevo_diagnostico.save()
            
            equipo_obj.estado = 'Diagnosticado'
            equipo_obj.save()
            return redirect(f"/entrega/reporte/?cliente={equipo_obj.cliente}")
        
        except Equipo.DoesNotExist:
            contexto = { 'equipos_pendientes': Equipo.objects.filter(estado='Recibido'), 'error': 'Equipo no encontrado.' }
            return render(request, 'DiagnosticoApp/evaluar_equipo.html', contexto)

    equipo_a_evaluar = None
    error_get = None
    equipo_id_get = request.GET.get('equipo_id')
    if not equipo_id_get:
        return redirect('asignar_tecnico')
    
    try:
        equipo_a_evaluar = Equipo.objects.get(id=equipo_id_get, estado='Recibido')
        contexto = {
            'equipo': equipo_a_evaluar,
        }
        return render(request, 'DiagnosticoApp/evaluar_equipo.html', contexto) 
    except Equipo.DoesNotExist:
        return redirect('asignar_tecnico')
  
def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    
    todos_los_diagnosticos = Diagnostico.objects.all()
    contexto = { 'diagnosticos': todos_los_diagnosticos }
    return render(request, 'DiagnosticoApp/listado_diagnosticos.html', contexto)