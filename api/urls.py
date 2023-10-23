from django.urls import path, include
from rest_framework import routers
from api import views
from .views import VehiculoView

router=routers.DefaultRouter()
router.register(r'vehiculo',views.VehiculoViewSet)

urlpatterns=[
    path('', include(router.urls)),
    ]