from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from comercio.models import Productos,RegistroMayoristas,Sorteo
from comercio.forms import FormularioBusqueda,FormularioMayoristas

# Create your views here.
def index(request):

    listado_productos= Productos.objects.all()

    if request.GET.get("nombre_producto"):
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos= Productos.objects.filter(nombre__icontains = data["nombre_producto"])
            return render(request,"comercio/index.html",{"productos": listado_productos,"formulario":formulario})

    else:
        formulario = FormularioBusqueda()
        return render(request,"comercio/index.html",{"productos": listado_productos, "formulario":formulario})
   
def crear_mayorista(request):
    if request.method =="GET":
        return render(request,"comercio/formulario.html")
    else:
        nombre = request.POST["nombre"]
        empresa = request.POST["empresa"]
        correo = request.POST["correo"]
        mayoristas =RegistroMayoristas(nombre=nombre,empresa=empresa,correo=correo)
        mayoristas.save()
        return render(request,"comercio/index.html")

def crear_sorteo(request):
    if request.method =="GET":
        return render(request,"comercio/formulario_sorteo.html")
    else:
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        localidad = request.POST["localidad"]
        sorteo =Sorteo(nombre=nombre,correo=correo,localidad=localidad)
        sorteo.save()
        return render(request,"comercio/index.html")

def cargar_producto(request):
    if request.method =="GET":
        return render(request,"comercio/cargar_producto.html")
    else:
        nombre = request.POST["nombre"]
        material = request.POST["material"]
        precio = request.POST["precio"]
        producto_nuevo =Productos(nombre=nombre,material=material,precio=precio)
        producto_nuevo.save()
        return render(request,"comercio/index.html")
