from django.forms import Form,CharField,IntegerField,EmailField
from django.db import models
from django.db.models import CharField,FloatField,EmailField

class FormularioBusqueda(Form):
    nombre_producto = CharField(max_length=150)

class FormularioMayoristas(Form):
    nombre = CharField(max_length=80)
    correo = EmailField(max_length=100)
    empresa = CharField(blank=True,null=True,max_length=100)
