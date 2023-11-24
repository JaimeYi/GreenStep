from rest_framework import viewsets, filters
from .serializer import VehiculoSerializer
from .models import Vehiculo
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import requests


# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            vehiculo=list(Vehiculo.objects.filter(id=id).values())
            if len(vehiculo)>0:
                vehiculo=vehiculo[0]
                datos={'message': 'Success','vehiculo':vehiculo}
            else:
                datos={'message': 'Datos no encontrados'}
            return JsonResponse(datos)
        else:
            vehiculo=list(Vehiculo.objects.values())
            if len(vehiculo)>0:
                datos={'message': 'Success','vehiculo':vehiculo}
            else:
                datos={'message': 'Datos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Vehiculo.objects.create(tipo_de_vehiculo= jd['tipo_de_vehiculo'], tipo_de_combustible= jd['tipo_de_combustible'], carbono_por_litro= jd['carbono_por_litro'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        vehiculo=list(Vehiculo.objects.filter(id=id).values())
        if len(vehiculo)>0:
            vehiculo=Vehiculo.objects.get(id=id)
            vehiculo.tipo_de_vehiculo= jd['tipo_de_vehiculo']
            vehiculo.tipo_de_combustible= jd['tipo_de_combustible']
            vehiculo.carbono_por_litro= jd['carbono_por_litro']
            vehiculo.save()
            datos={'message': 'Success'}
        else:
            datos={'message': 'Datos no encontrados'}
        return JsonResponse(datos)

    def delete(self, request, id):
        vehiculo=list(Vehiculo.objects.filter(id=id).values())
        if len(vehiculo)>0:
            Vehiculo.objects.filter(id=id).delete()
            datos={'message': 'Success'}
        else:
            datos={'message': 'Datos no encontrados'}
        return JsonResponse(datos)
#############################################################