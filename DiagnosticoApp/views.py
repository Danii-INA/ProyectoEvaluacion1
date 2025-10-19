# DiagnosticoApp/views.py
from django.shortcuts import render, redirect
from RecepcionApp.views import equipos_recibidos

# Listas que simulan base de datos
asignaciones = []
diagnosticos_realizados = []

def asignar_tecnico(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    mensaje = None # Esta variable ya no se usará
    if 'estudiante' in request.GET and 'equipo_cliente' in request.GET:
        estudiante = request.GET.get('estudiante')
        cliente_equipo = request.GET.get('equipo_cliente')

        nueva_asignacion = { "estudiante": estudiante, "cliente": cliente_equipo }
        asignaciones.append(nueva_asignacion)

        # Redirigimos a la página de evaluar.
        return redirect(f"/diagnostico/evaluar/?cliente={cliente_equipo}&estudiante={estudiante}")

    # Si la petición es GET pero SIN datos (solo cargar la página), muestra el formulario
    contexto = { 'equipos': equipos_recibidos }
    return render(request, 'DiagnosticoApp/asignar_tecnico.html', contexto)

def evaluar_equipo(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    # mensaje = None # Ya no se necesita

    if request.method == 'POST':
        asignacion_str = request.POST.get('asignacion')
        diagnostico_txt = request.POST.get('diagnostico')
        solucion_txt = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')

        # Extraemos el nombre del estudiante y del cliente
        try: # Añadí un try/except para más seguridad
            estudiante, cliente = asignacion_str.split(' - ')
        except ValueError:
             # Si el formato es incorrecto, vuelve a mostrar el formulario con un error
             contexto = { 'asignaciones': asignaciones, 'error': 'Formato de asignación inválido.' }
             return render(request, 'DiagnosticoApp/evaluar_equipo.html', contexto)


        nuevo_diagnostico = {
            "estudiante": estudiante.strip(),
            "cliente": cliente.strip(),
            "diagnostico": diagnostico_txt,
            "solucion": solucion_txt,
            "tipo_solucion": tipo_solucion
        }
        diagnosticos_realizados.append(nuevo_diagnostico)
        # --- Mejora en el flujo :D ---
        # Redirigimos a la página de registrar entrega.
        return redirect(f"/entrega/reporte/?cliente={cliente.strip()}")

    # Si la petición es GET (solo cargar la página), muestra el formulario
    contexto = { 'asignaciones': asignaciones }
    return render(request, 'DiagnosticoApp/evaluar_equipo.html', contexto)


def listado_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    
    contexto = { 'diagnosticos': diagnosticos_realizados }
    return render(request, 'DiagnosticoApp/listado_diagnosticos.html', contexto)