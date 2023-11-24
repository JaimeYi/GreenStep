from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Encuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    kms_conducidos = models.IntegerField()
    promedio_electricidad = models.IntegerField()
    vuelos = models.IntegerField()
    carnes_rojas = models.IntegerField()
    reciclaje = models.IntegerField()
    transporte = models.IntegerField()
    jardin = models.IntegerField()
    agua_promedio = models.IntegerField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    suma_puntaje = models.IntegerField()
    carbono_generado = models.DecimalField(decimal_places=3, max_digits=7)

class Carbono(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carbono_auto = models.DecimalField(decimal_places=6, max_digits=7) #7.15 * 10^-3 ->0| 1,43 * 10^-2 -> 1| 2.86 * 10^-2
    carbono_electricidad = models.DecimalField(decimal_places=6, max_digits=7) #7.09 × 10^-4 toneladas métricas de CO2/kWh
    carbono_vuelos = models.DecimalField(decimal_places=6, max_digits=7) #2,85 × 10^-4 toneladas × 3000km 
    carne = models.DecimalField(decimal_places=6, max_digits=7) #6,625 * 10^-4 toneladas por cada 250 grs
    reciclaje_c = models.DecimalField(decimal_places=6, max_digits=7) #-8.33 * 10^-3 prom 
    transporte_publico = models.DecimalField(decimal_places=6, max_digits=7) #5.704 * 10^-4 prom
    jardin_c = models.DecimalField(decimal_places=6, max_digits=7)#-1.3 10^-4 prom
    agua = models.DecimalField(decimal_places=6, max_digits=7) #2.3 * 10^-2 prom
    fecha_respuesta = models.DateTimeField(auto_now_add=True)