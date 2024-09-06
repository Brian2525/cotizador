from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User, Group, Permission


class Status(models.Model):
    nombre=models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
    class Meta: 
        db_table='status'
        verbose_name='Status'
        verbose_name_plural='Status'
        ordering=['id']



class Categoria(models.Model):
    nombre=models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
    class Meta: 
        db_table='categories'
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['id']

class Check(models.Model):
    nombre_gerente = models.CharField(max_length=100, null=True)
    numero_cotizacion = models.IntegerField(null=True,  blank=True)
    nombre_empresa = models.CharField(max_length=100, null=True, blank=True ) 
    nombre_proyecto = models.CharField(max_length=100, null=True, blank=True)
    volumen_estimado = models.IntegerField(null=True,blank=True)
    numero_tintas = models.IntegerField(null=True, blank=True)
    tecnologia_fabricacion = models.CharField(max_length=100, null=True, blank=True)
    lugar_entrega = models.CharField(max_length=100, null=True, blank=True)
    producto_nuevo = models.BooleanField(default=False, null=True, blank=True)
    fecha_solicitud = models.DateField(null=True, blank=True)
    precio_objetivo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tipo_producto = models.CharField(max_length=100, null=True, blank=True)
    comentarios_adicionales = models.TextField(blank=True, null=True)
    frecuencia_compra = models.CharField(blank=True, max_length=100, null=True)
    estatus=models.ManyToManyField(Status, related_name='status', blank=True)
    motivo_rechazo =models.CharField( blank=True, max_length=100)
    autor=models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    fecha_expiracion=models.DateTimeField(default=timezone.now() + timedelta (minutes=3))
    vigente=models.BooleanField(default=True, null=True) #Vigencia del check
    cliente=models.CharField(max_length=100, null=True,  blank=True)
    categoria=models.ManyToManyField(Categoria, related_name='relevancia_check', blank=True) # relevancia de la categoria


    def save(self, *args, **kwargs):
        if not self.pk and 'user' in kwargs:
            self.author = kwargs.pop('user')
        super(Check, self).save(*args, **kwargs)

    def verificar_expiracion(self):
        if self.fecha_expiracion< timezone.now():
            self.vigente=False
            self.save()
    
    def renovar_expiracion(self):
        self.fecha_expiracion= timezone.now() + timedelta(minutes=3)
        self.vigente=True
        self.save()

    #def rechazo(self):
     #   self.motivo_rechazo= models.CharField(blank=True, max_length=100)
      #  self.save()


    

    def __str__(self):
        return self.nombre_proyecto  # Devuelve el nombre del producto como representación del objetouser=User.objects.create_user('username', 'mail', 'password')



