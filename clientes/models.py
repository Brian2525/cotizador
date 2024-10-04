from django.db import models




class Cliente(models.Model):
    ETAPAS = [
        ('inicial', 'Inicial'),
        ('primer_contacto', 'Primer Contacto'),
        ('seguimiento', 'Seguimiento'),
        ('propuesta_enviada', 'Propuesta Enviada'),
        ('cerrado', 'Cerrado'),
        ('perdido', 'Perdido'),
    ]

    nombre = models.CharField(max_length=255)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15)
    empresa = models.CharField(max_length=255)  # En el futuro podría ser una ForeignKey a Empresa
    posicion=models.CharField(max_length=255)
    encargado_cuenta = models.CharField(max_length=255)
    etapa = models.CharField(max_length=50, choices=ETAPAS, default='inicial')

    def __str__(self):
        return f"{self.nombre} - {self.etapa}"
    

    
class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    sitio_web = models.URLField(blank=True, null=True)
    contactos=models.ManyToManyField(Cliente) 

    def __str__(self):
        return self.nombre
