from django.db import models
from django.db.models import CharField,FloatField,EmailField

class Productos(models.Model):
    nombre =models.CharField(max_length=150)
    material = models.CharField(max_length=100)
    precio = models.FloatField()

    def __Str__(self):
        return f"{self.nombre} - de {self.material}"

class RegistroMayoristas(models.Model):
    nombre = models.CharField(max_length=80)
    correo = models.EmailField(max_length=100)
    empresa = models.CharField(blank=True,null=True,max_length=100)

    def __str__(self):
        return f"{self.empresa} - {self.nombre} - {self.correo}"

class Sorteo(models.Model):
    nombre = models.CharField(max_length=80)
    correo = models.CharField (max_length=80)
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"