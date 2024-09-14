from django.db import models

# Create your models here.

class Cliente(models.Model):
    STATUS_PIPELINE = [('Nuevo', 'Nuevo'),('Primer-contacto', 'Primer-contacto'),('Pendiente-de-respuesta', 'Pendiente-de-respuesta'),('Recordatorio-enviado', 'Recordatorio-enviado'),('Reunion-programada', 'Reunion-programada'),('Interesado', 'Interesado'),('Propuesta-en-revision', 'Propuesta-en-revision'),('Negociacion-activa', 'Negociacion-activa'),('interaccion-perdida', 'interaccion-perdida'),('Venta-cerrada', 'Venta-cerrada'),('Cliente-inactivo', 'Cliente-inactivo'),('Venta-perdida', 'Venta-perdida'),('Renovacion-o-actualicion', 'Renovacion-o-actualicion')]
 
    nombre_cliente = models.CharField(max_length=100, null=True, blank=True )
    empresa_cliente = models.CharField(max_length=100, null=True )
    direccion_cliente= models.CharField(max_length=100, null=True )
    telefono_cliente= models.IntegerField(null=True)
    email_cliente= models.CharField(max_length=100, null=True )
    propietario=models.IntegerField(blank=True, null=True)     #Hace falta poder asignar al vendedor.
    estado_pipeline=models.CharField(max_length=24, choices=STATUS_PIPELINE, default='Nuevo', blank=True)

    
    #Hace falta poder elegir un template. (En caso de tener catalogo de productos a elegir)
    #Hace falta que se pueda conocer el origen de el lead - ( puede ser que seleccionen con una imagen o puede ser que seleccionen desde un dropdown.
    

    def __str__(self):
        return self.nombre_cliente  # Devuelve el nombre del producto como representación del objetouser=User.objects.create_user('username', 'mail', 'password')
