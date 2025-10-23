from django.shortcuts import render, redirect
from RecepcionApp.models import Equipo
from DiagnosticoApp.models import Diagnostico
from .models import Entrega

def verificar_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    equipo_encontrado, diagnostico_encontrado, mensaje_error = None, None, None

    if 'cliente_busqueda' in request.GET:
        cliente_a_buscar = request.GET.get('cliente_busqueda')
        try:
            equipo_encontrado = Equipo.objects.get(cliente__iexact=cliente_a_buscar)
            diagnostico_encontrado = Diagnostico.objects.filter(equipo=equipo_encontrado).last()
        except Equipo.DoesNotExist:
            mensaje_error = f"No se encontró ningún equipo registrado para el cliente '{cliente_a_buscar}'."

    contexto = {
        'equipo': equipo_encontrado,
        'diagnostico': diagnostico_encontrado,
        'not_found': mensaje_error
    }
    return render(request, 'EntregaApp/verificar_entrega.html', contexto)


def reporte_entrega(request):
    if not request.session.get('autenticado'):
        return redirect('login')

    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        estado_final = request.POST.get('estado_final')
        observaciones = request.POST.get('observaciones')

        try:
            equipo_obj = Equipo.objects.get(cliente=cliente)

            entrega_obj, created = Entrega.objects.get_or_create(
                equipo=equipo_obj,
                defaults={'estado_final': estado_final, 'observaciones': observaciones}
            )
            if not created:
                entrega_obj.estado_final = estado_final
                entrega_obj.observaciones = observaciones
                entrega_obj.save()

            equipo_obj.estado = estado_final
            equipo_obj.save()

            return redirect(f"/entrega/verificar/?cliente_busqueda={cliente}")

        except Equipo.DoesNotExist:
            mensaje = f"Error: No se encontró equipo para el cliente '{cliente}'."
            diagnosticos_con_equipo = Diagnostico.objects.select_related('equipo').all()
            
            contexto = { 
                        'diagnosticos': diagnosticos_con_equipo, 
                        'mensaje': mensaje,
                        'is_error': True 
                        } 
            return render(request, 'EntregaApp/reporte_entrega.html', contexto)

    diagnosticos_con_equipo = Diagnostico.objects.select_related('equipo').filter(equipo__estado='Diagnosticado')
    contexto = { 'diagnosticos': diagnosticos_con_equipo }
    return render(request, 'EntregaApp/reporte_entrega.html', contexto)



def comprobante_entrega(request, cliente):
    if not request.session.get('autenticado'):
        return redirect('login')

    try:
        equipo_info = Equipo.objects.get(cliente__iexact=cliente)
        diagnostico_info = Diagnostico.objects.filter(equipo=equipo_info).last()
        entrega_info = Entrega.objects.filter(equipo=equipo_info).first()
    except Equipo.DoesNotExist:
        equipo_info, diagnostico_info, entrega_info = None, None, None
        
    contexto = {
        'equipo': equipo_info,
        'diagnostico': diagnostico_info,
        'entrega': entrega_info
    }
    return render(request, 'EntregaApp/comprobante_entrega.html', contexto)