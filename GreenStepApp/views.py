from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from api.models import Vehiculo
from .models import Encuesta

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def calculadora(request):
    vehiculos = Vehiculo.objects.all()
    return render (request, 'calculadora.html', {"vehiculos": vehiculos})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def mundo(request):
    return render(request, 'mundo.html')

@login_required
def nosotros(request):
    return render(request, 'nosotros.html')

@login_required
def calculo(request):
    return render(request, 'calculo.html')

@login_required
def calcularhuella(request):
    variables = [
        "kms_conducidos",
        "promedio_electricidad",
        "vuelos",
        "carnes_rojas",
        "reciclaje",
        "transporte",
        "jardin",
        "agua_promedio"
    ]
    suma = 0
    #esta parte suma los valores del formulario y lo encasilla en un intervalo 
    for i in variables:
        suma += int(request.GET[i])
    if suma >= 4:
        carbono = "bajo"
    elif 4 < suma <= 10:
        carbono = "moderada"
    else:
        carbono = "alto"
    mensaje = f"Su huella de carbono es {carbono}, puntaje: {suma}"
    #esta parte guarda los datos introducidos en el formulario y los sube a la base de datos
    encuesta = Encuesta(
        usuario = request.user,
        kms_conducidos = int(request.GET["kms_conducidos"]),
        promedio_electricidad = int(request.GET["promedio_electricidad"]),
        vuelos = int(request.GET["vuelos"]),
        carnes_rojas = int(request.GET["carnes_rojas"]),
        reciclaje = int(request.GET["reciclaje"]),
        transporte = int(request.GET["transporte"]),
        jardin = int(request.GET["jardin"]),
        agua_promedio = int(request.GET["agua_promedio"]),
        suma_puntaje = suma
    )
    encuesta.save()

    tipo = request.GET["tipo_de_vehiculo"]
    print(tipo)

    return render(request, 'calculo.html', {'mensaje': mensaje})