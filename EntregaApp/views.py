# EntregaApp/views.py
from django.shortcuts import render, redirect

from RecepcionApp.views import equipos_recibidos
from DiagnosticoApp.views import diagnosticos_realizados

entregas_finalizadas = []

def verificar_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    equipo_encontrado, diagnostico_encontrado, mensaje_error = None, None, None

    if 'cliente_busqueda' in request.GET:
        cliente_a_buscar = request.GET.get('cliente_busqueda')
        for equipo in equipos_recibidos:
            if equipo['cliente'].lower() == cliente_a_buscar.lower():
                equipo_encontrado = equipo
                break
        
        if equipo_encontrado:
            for diagnostico in diagnosticos_realizados:
                if diagnostico['cliente'].lower() == cliente_a_buscar.lower():
                    diagnostico_encontrado = diagnostico
                    break
        else:
            mensaje_error = f"No se encontró ningún equipo registrado para el cliente '{cliente_a_buscar}'."

    contexto = { 'equipo': equipo_encontrado, 'diagnostico': diagnostico_encontrado, 'not_found': mensaje_error }
    return render(request, 'EntregaApp/verificar_entrega.html', contexto)

def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    # --- (Procesar el formulario) ---
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        estado_final = request.POST.get('estado_final')
        observaciones = request.POST.get('observaciones')

        nuevo_reporte = { "cliente": cliente, "estado": estado_final, "observaciones": observaciones }
        entregas_finalizadas.append(nuevo_reporte)

        for equipo in equipos_recibidos:
            if equipo['cliente'] == cliente:
                equipo['estado'] = estado_final
                break
        
        # redirige la página de verificar
        return redirect(f"/entrega/verificar/?cliente_busqueda={cliente}")

    # --- Lógica para GET (Mostrar el formulario) ---
    contexto = { 'diagnosticos': diagnosticos_realizados }
    return render(request, 'EntregaApp/reporte_entrega.html', contexto)

def comprobante_entrega(request, cliente):
    if not request.session.get('autenticado'):
        return redirect('login')

    # Buscamos toda la información del cliente especificado en la URL
    equipo_info = next((eq for eq in equipos_recibidos if eq['cliente'] == cliente), None)
    diagnostico_info = next((diag for diag in diagnosticos_realizados if diag['cliente'] == cliente), None)
    entrega_info = next((ent for ent in entregas_finalizadas if ent['cliente'] == cliente), None)

    contexto = {
        'equipo': equipo_info,
        'diagnostico': diagnostico_info,
        'entrega': entrega_info
    }
    return render(request, 'EntregaApp/comprobante_entrega.html', contexto)