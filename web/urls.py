from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'), #responde a la funcion index de view.py
    path("nueva_tarea/", views.nueva_tarea, name="nueva_tarea") #response a la funcion nueva_tarea de view.py
]
