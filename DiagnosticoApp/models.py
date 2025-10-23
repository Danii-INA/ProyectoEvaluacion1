from django.db import models
from RecepcionApp.models import Equipo 

class Diagnostico(models.Model):
    # Relación "Uno a Muchos": Un Equipo puede tener varios Diagnósticos)
    # pero un Diagnóstico pertenece a un solo Equipo.
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    estudiante = models.CharField(max_length=100) 
    diagnostico_problema = models.TextField() 
    solucion = models.TextField() 
    tipo_solucion = models.CharField(max_length=50) 
    fecha_diagnostico = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Diagnóstico para {self.equipo.cliente} por {self.estudiante}"
