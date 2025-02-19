from django.db import models
from django.contrib.auth.models import User



class ContactForm(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    empresa = models.CharField(max_length=255, blank=True)  # Opcional, puede ser dejado en blanco
    telefono = models.CharField(max_length=20, blank=True)  # Opcional, puede ser dejado en blanco
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se registra automáticamente al crear un objeto

    def __str__(self):
        return f"{self.nombre} - {self.email}"



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
    empresa = models.CharField(max_length=255, null=True, blank=True)
    asunto=models.CharField(max_length=255, null=True, blank=True)
    posicion = models.CharField(max_length=255, null=True, default='Desconocido')
    etapa = models.CharField(max_length=50, choices=ETAPAS, default='inicial')

    def __str__(self):
        return f"{self.nombre} - {self.etapa}"
    
