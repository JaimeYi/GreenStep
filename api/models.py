from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehiculo(models.Model):
    tipo_de_vehiculo = models.CharField(max_length=100)
    tipo_de_combustible = models.CharField(max_length=50)
    carbono_por_litro = models.PositiveIntegerField() #esta en gramos

class Carbono(models.Model):
    carbono_electricidad = models.DecimalField(decimal_places=6, max_digits=7) #7.09 × 10^-4 toneladas métricas de CO2/kWh
    carbono_vuelos = models.DecimalField(decimal_places=6, max_digits=7) #2,85 × 10^-4 toneladas × km 
    carne = models.DecimalField(decimal_places=6, max_digits=7)
    reciclaje = models.DecimalField(decimal_places=6, max_digits=7)
    transporte_publico = models.DecimalField(decimal_places=6, max_digits=7)
    jardin = models.DecimalField(decimal_places=6, max_digits=7)
    agua = models.DecimalField(decimal_places=6, max_digits=7)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'