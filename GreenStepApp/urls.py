from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('huella_de_carbono/', views.calculadora, name='calculadora'),
    ]