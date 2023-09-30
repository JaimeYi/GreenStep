from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def indexView(request):
    return render(request, 'index.html')