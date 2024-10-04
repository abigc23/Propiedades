#--->Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import *

class NuevaPropiedad(forms.ModelForm):
    class Meta:
        model=Propiedad
        fields='__all__'