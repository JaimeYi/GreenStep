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