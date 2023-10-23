from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('huella_de_carbono/', views.calculadora, name='calculadora'),
    ]