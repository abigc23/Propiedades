from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def Home(request):
    propiedades = Propiedad.objects.all().order_by('-codigo')[:3] 
    data = {
        'propiedades': propiedades 
    }
    return render(request, 'index.html', data)

def ver_Propiedades(request):
    propiedades = Propiedad.objects.all()
    data = {
        'propiedades': propiedades  
    }
    return render(request, 'pages/propiedades.html', data)

def detalles_propiedad(request, codigo):
    propiedad = get_object_or_404(Propiedad, codigo=codigo) 
    return render(request, 'pages/detallesprop.html', {'propiedad': propiedad})