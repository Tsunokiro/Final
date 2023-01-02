from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length = 150)
    nombre = models.CharField(max_length = 150)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    estado = models.CharField(max_length = 1)
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField (max_length = 50)
    nombre_corto = models.CharField (max_length = 10)
    imagen = models.ImageField (upload_to='fotos', null=True)
    estado = models.CharField (max_length = 1)
    def __str__(self):
        return self.nombre