from django.shortcuts import render, redirect
from .forms import NewRegister

# Create your views here.

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
        
    return render(request, 'registration/register.html',{'form':NewRegister})