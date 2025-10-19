# RecepcionApp/views.py
from django.shortcuts import render, redirect

# Esta lista simulará nuestra "base de datos" por ahora
equipos_recibidos = []

def registrar_equipo(request):
    # Proteger la vista: si el usuario no está autenticado, se va al login
    if not request.session.get('autenticado'):
        return redirect('login')

    mensaje_exito = None
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        cliente = request.POST.get('cliente')
        tipo_equipo = request.POST.get('tipo_equipo')
        problema = request.POST.get('problema')

        # Creamos un diccionario para el nuevo equipo
        nuevo_equipo = {
            "cliente": cliente,
            "equipo": tipo_equipo,
            "problema": problema,
            "estado": "Recibido" # Añadimos un estado inicial
        }

        # Añadimos el diccionario a nuestra lista
        equipos_recibidos.append(nuevo_equipo)

        # Preparamos un mensaje de confirmación para mostrarlo en la página
        mensaje_exito = "¡Equipo registrado exitosamente!"
        # Redirigimos a la página de asignar, pasando el nombre del cliente
        return redirect(f"/diagnostico/asignar/?equipo_cliente={cliente}")

    return render(request, 'RecepcionApp/registrar_equipo.html')

# Mantenemos las otras vistas como esqueletos por ahora
def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('login')
    
    contexto = {'equipos': equipos_recibidos}
    return render(request, 'RecepcionApp/listado_equipos.html', contexto)

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('login')
        
    # Lógica simple para encontrar el equipo (mejoraría en un proyecto real)
    equipo_encontrado = None
    for equipo in equipos_recibidos:
        if equipo['cliente'].lower() == nombre.lower():
            equipo_encontrado = equipo
            break

    return render(request, 'RecepcionApp/detalle_equipo.html', {'equipo': equipo_encontrado})