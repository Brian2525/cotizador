from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime
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
    STATUS_CHOICES = [('pendiente', 'pendiente'),('aprobado', 'aprobado'),('rechazado', 'rechazado')]
    PRODUCT_CLASIFICATIOM= [('si', 'si'),('no', 'no')]

    nombre_gerente = models.CharField(max_length=100, null=True)
    numero_cotizacion = models.IntegerField(max_length=10, null=True,  blank=True)
    nombre_empresa = models.CharField(max_length=100, null=True, blank=True ) 
    nombre_proyecto = models.CharField(max_length=100, null=True, blank=True)
    volumen_estimado = models.IntegerField(null=True,blank=True)
    numero_tintas = models.IntegerField(null=True, blank=True)
    tecnologia_fabricacion = models.CharField(max_length=100, null=True, blank=True)
    lugar_entrega = models.CharField(max_length=100, null=True, blank=True)
    producto_nuevo = models.BooleanField(default=False, null=True, blank=True)
    fecha_solicitud = models.DateTimeField(default=datetime.now())
    precio_objetivo = models.IntegerField(max_length=10, null=True, blank=True)
    tipo_producto = models.CharField(max_length=100, null=True, blank=True)
    comentarios_adicionales = models.TextField(max_length=300, blank=True, null=True) #por si existe algun requerimiento en especifico para el proyecto
    frecuencia_compra = models.CharField(blank=True, max_length=100, null=True)
    estatus=models.ManyToManyField(Status, related_name='status', blank=True) # El estatus se refiere al estado en el pipeline de ventas 
    estado=models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendiente', blank=True) #Este estado se refiere a la clasificacion de IDI. 
    motivo_rechazo =models.CharField( blank=True, max_length=100)
    autor=models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    fecha_expiracion=models.DateTimeField(default=timezone.now() + timedelta (days=10))
    vigente=models.BooleanField(default=True, null=True) #Vigencia del check
    cliente=models.CharField(max_length=100, null=True,  blank=True)
    categoria=models.ManyToManyField(Categoria, related_name='relevancia_check', blank=True) # relevancia de la categoria
    #Version del check - cada que haya un rechazo o debe agrearse la version 1.1 
    


    def save(self, *args, **kwargs):
        if not self.pk and 'user' in kwargs:
            self.author = kwargs.pop('user')
        super(Check, self).save(*args, **kwargs)

    def verificar_expiracion(self):
        if self.fecha_expiracion< timezone.now():
            self.vigente=False
            self.save()
    
    def renovar_expiracion(self):
        self.fecha_expiracion= timezone.now() + timedelta(days=10)
        self.vigente=True
        self.save()

    #def rechazo(self):
     #   self.motivo_rechazo= models.CharField(blank=True, max_length=100)
      #  self.save()


    def __str__(self):
        return self.nombre_proyecto  # Devuelve el nombre del producto como representación del objetouser=User.objects.create_user('username', 'mail', 'password')



class Comentarios(models.Model):
    check_asociado=models.ForeignKey(Check, on_delete=models.CASCADE,related_name='comentarios', blank=True, null=True)
    autor_comentario=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    comentario=models.TextField(max_length=100, null=True)
    fecha_creacion=models.DateTimeField(default=datetime.now())
    resuelto=models.BooleanField(default=False, blank=True, null=True )

    
    def __str__(self):
        return self.comentario 





