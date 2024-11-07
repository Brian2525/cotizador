
from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    sitio_web = models.URLField(blank=True, null=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

