from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('huella_de_carbono/', views.calculadora, name='calculadora'),
    path('profile/', views.profile, name='profile'),
    path('tu_mundo/', views.mundo, name='mundo'),
    path('nosotros/', views.nosotros, name='nosotros'),
    ]