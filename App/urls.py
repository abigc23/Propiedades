from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    #-->URL, FUNCION, operacion PARA HTML
    path('',Home,name='inicio'),
    path('agregar/',Agregar,name='agregar'),
    path('propiedades/',ver_Propiedades,name='propiedades'),
    path('modificar/<codigo>/',Modificar_Propiedad,name='modificar'),
    path('eliminar/<codigo>/',Eliminar_Propiedad,name='eliminar'),
    path('logouts/',salir,name='logouts'),
]
