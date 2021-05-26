from django.shortcuts import render
from .models import Tarea

def index(request):
    return render(request, "web/index.html")

def nueva_tarea(request):
    nombre = request.GET["nombre"]
    
    Tarea(
        nombre=nombre,
    ).save()

    context = {"tareas": Tarea.objects.all()}

    # print(fecha_de_nacimiento)

    return render(request, "web/index.html", context=context)