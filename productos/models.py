
from django.db import models



class Producto(models.Model):
    PRODUCTO = 'producto'
    SERVICIO = 'servicio'
    TIPO_CHOICES = [
        (PRODUCTO, 'Producto'),
        (SERVICIO, 'Servicio'),
    ]
    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    sku = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, null=True)

    def __str__(self):
        return self.nombre
# Create your models here.
