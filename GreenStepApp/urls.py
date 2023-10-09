from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(),name="login_url"),
    path('register/', views.registerView,name='register_url',),
    path('logout/',LogoutView.as_view(),name='logout'),
    ]