from django.db import models

class Propiedad(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)  # Nombre de la propiedad
    tipo = models.CharField(max_length=30)  # Tipo de propiedad (ej. casa, departamento, etc.)
    ubicacion = models.CharField(max_length=100)  # Ubicación de la propiedad
    descripcion = models.TextField()  # Descripción de la propiedad
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de la propiedad
    imagen = models.ImageField(upload_to="propiedades/", null=True, blank=True)  # Imagen de la propiedad
    superficie_total = models.DecimalField(max_digits=10, decimal_places=2)  # Superficie total en m2
    superficie_cubierta = models.DecimalField(max_digits=10, decimal_places=2)  # Superficie cubierta en m2
    ambientes = models.IntegerField()  # Número de ambientes
    plantas = models.IntegerField()  # Número de plantas
    dormitorios = models.IntegerField()  # Número de dormitorios
    baños = models.IntegerField()  # Número de baños
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  # Fecha de publicación

    def __str__(self):
        return self.nombre
