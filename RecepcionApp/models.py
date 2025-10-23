from django.db import models

class Equipo(models.Model):
    cliente = models.CharField(max_length=100)
    tipo_equipo = models.CharField(max_length=100)
    problema = models.TextField()
    estado = models.CharField(max_length=50, default='Recibido')
    fecha_recepcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Equipo de {self.cliente} ({self.tipo_equipo})"