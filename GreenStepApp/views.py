from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from .models import Encuesta, Carbono
import json
from login.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def home(request):
    datos = Encuesta.objects.filter(usuario=request.user)
    carbono = datos.values_list('carbono_generado', flat=True)
    if len(carbono) == 0:
        carbono = str(0)
        message = "Sin registro"
    else:
        carbono = str(carbono[len(carbono)-1])
        carbono = carbono.replace('.',',')
        message = f"{carbono} toneladas"
    return render(request, 'home.html', {'message': message, 'carbono': carbono})

@login_required
def calculadora(request):
    return render (request, 'calculadora.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Tu cuenta ha sido actualizada correctamente')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    if request.user.is_authenticated:
        respuestas_usuario = Encuesta.objects.filter(usuario=request.user)
        label = []
        data =[]
        cantidad_de_respuesta = ""
        respuestas=len(respuestas_usuario)
        temp = 0
        prom = 0
        cont = 0

        if len(respuestas_usuario) == 0:
            label.append('Sin registro')
            data.append(0)
            cantidad_de_respuesta = "0"
        elif 0 < len(respuestas_usuario) < 5:
            for i in respuestas_usuario:
                fecha = str(i.fecha_respuesta)
                fecha = fecha[:16]
                data.append(float(i.carbono_generado))
                label.append(fecha)
        elif len(respuestas_usuario) >= 5:
            for i in respuestas_usuario[len(respuestas_usuario)-5:]:
                fecha = str(i.fecha_respuesta)
                fecha = fecha[:16]
                data.append(float(i.carbono_generado))
                label.append(fecha)
        for x in respuestas_usuario:
            cont += 1
            temp += float(x.carbono_generado)
        if temp == 0:
            temp = '0'
            prom = f'{temp} Ton'
        else:
            temp = str(round(temp/cont, 3))
            temp = temp.replace('.',',')
            prom = f'{temp} Ton'

        labels_json = json.dumps(label)
        data_json = json.dumps(data)

        return render(request, 'profile.html', {'labels': labels_json, 'data': data_json, 'respuestas': cantidad_de_respuesta, 'u_form': u_form, 'p_form': p_form, 'cr':respuestas, 'prom': prom})
    
    return render(request, 'profile.html', {'respuestas': "none", 'u_form': u_form, 'p_form': p_form, 'cr':respuestas, 'prom': prom})

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
    carbono_total = 0

    for m in variables:
        if m == "kms_conducidos":
            if int(request.GET[m]) == 0:
                carbono_auto = 0.00715
                carbono_total += carbono_auto
            elif int(request.GET[m]) == 1:
                carbono_auto = 0.0143
                carbono_total += carbono_auto
            else:
                carbono_auto = 0.0286
                carbono_total += carbono_auto
        elif m == "promedio_electricidad":
            if int(request.GET[m]) == 0:
                carbono_electricidad = 0.000709*100
                carbono_total += carbono_electricidad
            elif int(request.GET[m]) == 1:
                carbono_electricidad = 0.000709*200
                carbono_total += carbono_electricidad
            else:
                carbono_electricidad = 0.000709*300
                carbono_total += carbono_electricidad
        elif m == "vuelos":
            if int(request.GET[m]) == 0:
                carbono_vuelos = 0
                carbono_total += carbono_vuelos
            elif int(request.GET[m]) == 1:
                carbono_vuelos = 0.000285*4500
                carbono_total += carbono_vuelos
            else:
                carbono_vuelos = 0.000285*9000
                carbono_total += carbono_vuelos
        elif m == "carnes_rojas":
            if int(request.GET[m]) == 0:
                carne = 0.0006625
                carbono_total += carne
            elif int(request.GET[m]) == 1:
                carne = 0.0006625*2
                carbono_total += carne
            else:
                carne = 0.0006625*4
                carbono_total += carne
        elif m == "reciclaje":
            if int(request.GET[m]) == 0:
                reciclaje_c = 0
                carbono_total += reciclaje_c
            elif int(request.GET[m]) == 1:
                reciclaje_c = -0.0000833
                carbono_total += reciclaje_c
            else:
                reciclaje_c = -0.0000833*2
                carbono_total += reciclaje_c
        elif m == "transporte":
            if int(request.GET[m]) == 0:
                transporte_publico = 0.0005704
                carbono_total += transporte_publico
            elif int(request.GET[m]) == 1:
                transporte_publico = 0.0005704*2
                carbono_total += transporte_publico
            else:
                transporte_publico = 0.0005704*3
                carbono_total += transporte_publico
        elif m == "jardin":
            if int(request.GET[m]) == 0:
                jardin_c = 0
                carbono_total += jardin_c
            elif int(request.GET[m]) == 1:
                jardin_c = -0.000013
                carbono_total += jardin_c
            else:
                jardin_c = -0.000013*2
                carbono_total += jardin_c
        elif m == "agua_promedio":
            if int(request.GET[m]) == 0:
                agua = 0.023
                carbono_total += agua
            elif int(request.GET[m]) == 1:
                agua = 0.023*2
                carbono_total += agua
            else:
                agua = 0.023*3
                carbono_total += agua
    
    carbono_total = round(carbono_total, 3)

    carbono_general = Carbono(
        usuario = request.user,
        carbono_auto = carbono_auto,
        carbono_electricidad = carbono_electricidad,
        carbono_vuelos = carbono_vuelos,
        carne = carne,
        reciclaje_c = reciclaje_c,
        transporte_publico = transporte_publico,
        jardin_c = jardin_c,
        agua = agua
    )
    carbono_general.save()

    #esta parte suma los valores del formulario y lo encasilla en un intervalo 
    for i in variables:
        suma += int(request.GET[i])
    if suma <= 4:
        carbono = "bajo"
    elif 4 < suma <= 10:
        carbono = "moderada"
    else:
        carbono = "alto"
    mensaje = f"Su huella de carbono es {carbono}, puntaje: {suma}, carbono total: {carbono_total} toneladas"
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
        suma_puntaje = suma,
        carbono_generado = carbono_total
    )
    encuesta.save()

    messages.success(request, f'Muchas gracias por responder la encuesta, ya hemos recopilado tus datos, revisalos en la sección perfil')

    return render(request, 'calculo.html', {'mensaje': mensaje})

@login_required
def mundo(request):
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

    data =[]

    respuestas = Encuesta.objects.filter(usuario=request.user)
    if len(respuestas) == 0:
        respondio = 'no'
        return render(request, 'mundo.html', {'responde': respondio, 'data': ['none']})
    else:
        ultima_encuesta = respuestas[len(respuestas)-1]
        respondio = 'si'
        if ultima_encuesta.kms_conducidos == 2:
            data.append("kms_conducidos")
        if ultima_encuesta.promedio_electricidad == 2:
            data.append("promedio_electricidad")
        if ultima_encuesta.vuelos == 2:
            data.append("vuelos")
        if ultima_encuesta.carnes_rojas == 2:
            data.append("carnes_rojas")
        if ultima_encuesta.reciclaje == 0:
            data.append("reciclaje")
        if ultima_encuesta.transporte == 0:
            data.append("transporte")
        if ultima_encuesta.jardin == 0:
            data.append("jardin")
        if ultima_encuesta.agua_promedio == 2:
            data.append("agua_promedio")
        if len(data) == 0:
            data.append("felicidades")

        return render(request, 'mundo.html', {'responde': respondio, 'data': data})
