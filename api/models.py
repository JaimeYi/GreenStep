from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    tipo_de_vehiculo = models.CharField(max_length=100)
    tipo_de_combustible = models.CharField(max_length=50)
    carbono_por_litro = models.PositiveIntegerField() #esta en gramos
