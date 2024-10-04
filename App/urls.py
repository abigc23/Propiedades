from django.urls import path
from .views import *

urlpatterns = [
    #-->URL, FUNCION, operacion PARA HTML
    path('',Home,name='inicio'),
    path('propiedades/',ver_Propiedades,name='propiedades'),
    path('detallesprop/',ver_Propiedades,name='detallesprop'),
]
