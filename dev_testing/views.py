from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render

def Camera(request):
    return render(request, 'camera.html')

def Map(request):
    return render(request, 'map.html')
