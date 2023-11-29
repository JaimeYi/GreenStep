from django.shortcuts import render, redirect
from .forms import NewRegister
from django.contrib import messages

# Create your views here.

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta se ha creado exitosamente {username}')
            return redirect('login_url')
        else:
            messages.error(request, f'Nombre y/o contraseña incorrectos')
            form = NewRegister()
        
    return render(request, 'registration/register.html',{'form':NewRegister})
