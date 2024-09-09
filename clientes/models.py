from django.db import models

# Create your models here.

class Cliente(models.Model): 
    nombre_cliente = models.CharField(max_length=100, null=True, blank=True )
    empresa_cliente = models.CharField(max_length=100, null=True )
    direccion_cliente= models.CharField(max_length=100, null=True )
    telefono_cliente= models.IntegerField(null=True)
    email_cliente= models.CharField(max_length=100, null=True )
    #Hace falta poder asignar al vendedor.
    

    def __str__(self):
        return self.nombre_cliente  # Devuelve el nombre del producto como representación del objetouser=User.objects.create_user('username', 'mail', 'password')
