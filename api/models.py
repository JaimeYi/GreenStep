from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    tipo_de_vehiculo = models.CharField(max_length=100)
    tipo_de_combustible = models.CharField(max_length=50)
    carbono_por_litro = models.PositiveIntegerField() #esta en gramos

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'