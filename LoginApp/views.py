# LoginApp/views.py
from django.shortcuts import render, redirect

def login_view(request):
    if request.session.get('autenticado'):
        return redirect('registrar_equipo') 

    error = None 

    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')

        if usuario == 'inacap' and clave == 'clinica2025':
            request.session['autenticado'] = True 
            request.session['username'] = usuario 
            return redirect('registrar_equipo') 
        else:
            error = "¡Usuario o clave incorrectos!" 

    
    return render(request, 'LoginApp/login.html', {'error_message': error})

def logout_view(request):
    request.session.flush()  
    return redirect('login') 