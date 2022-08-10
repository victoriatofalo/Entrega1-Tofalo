from django.urls import path
from comercio.views import index,crear_mayorista,crear_sorteo,cargar_producto

urlpatterns = [
    path("inicio/", index, name="Inicio"),
    path("mayoristas/",crear_mayorista, name="Mayorista"),
    path('sorteo/',crear_sorteo,name="sorteo"),
    path('producto/',cargar_producto,name="Cargar producto")    
    
]