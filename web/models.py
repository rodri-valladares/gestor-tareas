from django.db import models


class Tarea(models.Model):
    nombre = models.TextField()
