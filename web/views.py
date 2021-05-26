from django.shortcuts import render
from .models import Tarea

def index(request):
    return render(request, "web/index.html")
