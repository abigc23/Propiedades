from django.shortcuts import render,get_object_or_404,redirect
#---->Importamos el Sector de Formularios
from .forms import *
from .models import *
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def Home(request):
    buscar=Propiedad.objects.all().order_by('-codigo')[:3]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

def ver_Propiedades(request):
    #--->TREAMOS TODOS LOS ELEMENTOS DEL TABLA
    buscar=Propiedad.objects.all()
    data={
        'forms':buscar
    }
    return render(request,'Pages/propiedades.html',data)

@login_required

@permission_required('App.add_propiedad')
def Agregar(request):
    data={
        'forms':NuevaPropiedad()
    }
    if request.method=='POST':
        query=NuevaPropiedad(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['forms']=NuevaPropiedad
    return render (request,'Pages/agregar.html',data)


@permission_required('App.change_propiedad')
def Modificar_Propiedad(request,Codigo):
    sql=get_object_or_404(Propiedad,Codigo=Codigo)
    data={
        'forms':NuevaPropiedad(instance=sql)
    }
    if request.method=='POST':
        query=NuevaPropiedad(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Modificados Correctamente "
        else:
            data['forms']=NuevaPropiedad
    return render (request,'Pages/modificar.html',data)


@permission_required('App.delete_propiedad')
def Eliminar_Propiedad(request,Codigo):
    buscar=get_object_or_404(Propiedad,Codigo=Codigo)
    buscar.delete()
    return redirect(to="propiedades")


def salir(request):
    logout(request)
    return redirect(to='inicio')