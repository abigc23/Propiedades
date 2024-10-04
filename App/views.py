from django.shortcuts import render 
from .forms import *
from .models import *

# Create your views here.
def Home(request):
    buscar=Propiedad.objects.all().order_by('-codigo')[:3]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

def ver_Propiedades(request):
    buscar=Propiedad.objects.all()
    data={
        'forms':buscar
    }
    return render(request,'pages/propiedades.html',data)
