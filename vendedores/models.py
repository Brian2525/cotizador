
from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    sitio_web = models.URLField(blank=True, null=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

