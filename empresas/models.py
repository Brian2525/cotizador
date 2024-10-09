from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    sitio_web = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.nombre
