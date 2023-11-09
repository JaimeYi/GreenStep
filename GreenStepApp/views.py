from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from api.models import Vehiculo


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