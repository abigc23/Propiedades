from django.db import models

class Propiedad(models.Model):
    codigo = models.AutoField(primary_key=True)
    operacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)  # Ahora permite valores nulos o vacíos
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="propiedades/", null=True, blank=True)
    superficie_total = models.DecimalField(max_digits=10, decimal_places=2)
    superficie_cubierta = models.DecimalField(max_digits=10, decimal_places=2)
    ambientes = models.IntegerField()
    plantas = models.IntegerField()
    dormitorios = models.IntegerField()
    baños = models.IntegerField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.codigo
