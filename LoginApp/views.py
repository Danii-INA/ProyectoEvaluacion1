# LoginApp/views.py
from django.shortcuts import render, redirect

def login_view(request):
    # Si el usuario ya está autenticado, lo redirigimos para que no vea el login de nuevo
    if request.session.get('autenticado'):
        return redirect('registrar_equipo') # Redirigimos a la vista de registro en recepcion

    error = None # Variable para guardar el mensaje de error

    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')

        if usuario == 'inacap' and clave == 'clinica2025':
            request.session['autenticado'] = True # Se guarda la sesión si el usuario es válido
            return redirect('registrar_equipo') # se redirige a la página de registrar equipo
        else:
            error = "¡Usuario o clave incorrectos!" # Si falla, preparamos el mensaje de error

    # Si la petición es GET o si las credenciales fallaron, se muestra el formulario
    return render(request, 'LoginApp/login.html', {'error': error})