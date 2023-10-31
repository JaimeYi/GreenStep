from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from api.models import Vehiculo


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def calculadora(request):
    vehiculos = Vehiculo.objects.all()
    return render (request, 'calculadora.html', {"vehiculos": vehiculos})
