from django.db import models
from RecepcionApp.models import Equipo 

class Entrega(models.Model):
    # Relación "Uno a Uno": un Equipo solo tiene un registro de Entrega
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    
    estado_final = models.CharField(max_length=50) # 'Entregado', 'Pendiente', 'No Retirado'
    observaciones = models.TextField(blank=True, null=True)
    fecha_entrega = models.DateTimeField(auto_now_add=True) # Fecha del registro de entrega

    def __str__(self):
        return f"Entrega de equipo de {self.equipo.cliente} - Estado: {self.estado_final}"