# DiagnosticoApp/views.py
from django.shortcuts import render, redirect
from RecepcionApp.views import equipos_recibidos

# Listas que simulan base de datos
asignaciones = []
diagnosticos_realizados = []

def asignar_tecnico(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    mensaje = None
    if 'estudiante' in request.GET and 'equipo_cliente' in request.GET:
        estudiante = request.GET.get('estudiante')
        cliente_equipo = request.GET.get('equipo_cliente')

        nueva_asignacion = { "estudiante": estudiante, "cliente": cliente_equipo }
        asignaciones.append(nueva_asignacion)
        mensaje = f"¡Equipo de {cliente_equipo} asignado a {estudiante} exitosamente!"

    contexto = { 'equipos': equipos_recibidos, 'mensaje': mensaje }
    return render(request, 'DiagnosticoApp/asignar_tecnico.html', contexto)

def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    mensaje = None
    if request.method == 'POST':
        asignacion_str = request.POST.get('asignacion')
        diagnostico_txt = request.POST.get('diagnostico')
        solucion_txt = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')

        # Extraemos el nombre del estudiante y del cliente
        estudiante, cliente = asignacion_str.split(' - ')

        nuevo_diagnostico = {
            "estudiante": estudiante,
            "cliente": cliente,
            "diagnostico": diagnostico_txt,
            "solucion": solucion_txt,
            "tipo_solucion": tipo_solucion
        }
        diagnosticos_realizados.append(nuevo_diagnostico)
        mensaje = f"Diagnóstico para el equipo de {cliente} guardado correctamente."

    contexto = { 'asignaciones': asignaciones, 'mensaje': mensaje }
    return render(request, 'DiagnosticoApp/evaluar_equipo.html', contexto)


def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    
    contexto = { 'diagnosticos': diagnosticos_realizados }
    return render(request, 'DiagnosticoApp/listado_diagnosticos.html', contexto)