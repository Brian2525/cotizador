from django.db import models
from django.contrib.auth.models import User




class Cliente(models.Model):
    ETAPAS = [
        ('inicial', 'Inicial'),
        ('primer_contacto', 'Primer Contacto'),
        ('seguimiento', 'Seguimiento'),
        ('propuesta_enviada', 'Propuesta Enviada'),
        ('cerrado', 'Cerrado'),
        ('perdido', 'Perdido'),
        ('es_cliente', 'Es cliente'),
    ]

    nombre = models.CharField(max_length=255)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15)
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE, null=True, blank=True)  # En el futuro podría ser una ForeignKey a Empresa
    posicion=models.CharField(max_length=255, null=True, default='Desconocido')
    encargado_cuenta = models.ManyToManyField(User, null=True)
    etapa = models.CharField(max_length=50, choices=ETAPAS, default='inicial')

    def __str__(self):
        return f"{self.nombre} - {self.etapa}"
    
