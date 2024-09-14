from django.db import models


class Vendedores(models.Model): 
    nombre = models.CharField(max_length=100)
    numero_contacto = models.CharField(max_length=20, blank=True )
    email = models.EmailField(unique=True, blank=True)
    # Redes sociales
    facebook = models.URLField(blank=True, null=True)
    x_twitter = models.URLField(blank=True, null=True, verbose_name="X (Twitter)")
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    #sitio web y video 
    sitio_web = models.URLField(blank=True, null=True)
    video_corporativo = models.URLField(blank=True, null=True)
    #
    # origen= 
    #agregar de quien es este prospecto de acuerdo a su id
    #Seleccionar el tipo de producto o servicio de interes. 



    def __str__(self):
        return self.nombre
    
    #Tipo de plantilla a utilizar 
    #Agregar una imagen o campo para que seleccionen desde donde encontro el contacto - es decir el origen 



#class  plantillas 
#tipo de plantilla en la que se va a mostrar la informacion de los clientes, si es de producto(mas adelante) o si es de solo visualizacion. 


#El plan actual permite agregar un numero de vendedores por ejemplo 3.  
#La business card es la tarjeta de presentacion de cada uno de los vendedores. 
# class bc(models.Model):
# agregar vendedores 
# plantilla(sitio web)
# 
# 

#La business card debe contener la informacion de cada uno de los clientes, mi idea es que la empresa contrate esto y le pueda hacer una business card a cada vendedores.
#Cada vendedor puede tener su mini pagina, crear clientes y cotizaciones. 
#El precio por freelancer de hasta 1 usuarios  es de $900 anuales 99 mensuales por persona. 
# Equipos  $699 mensuales  por equipo de 5 personas. 
# Equipos de $1200 mensuales por equipo de 10 personas.





