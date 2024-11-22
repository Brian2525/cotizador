from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    presentacion = models.CharField(max_length=150, help_text="Máximo 30 palabras")

    def __str__(self):
        return f"Perfil de {self.usuario.username}"



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre



class Tag(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    contenido =RichTextField()
    imagen_thumbnail = models.ImageField(upload_to='blog/thumbanails/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_principal = models.ImageField(upload_to='blog/principal_image/', blank=True, null=True)

    def contar_palabras(self):
        return len(self.contenido.split())

    def tiempo_lectura(self):
        palabras_por_minuto = 200  # Puedes cambiarlo según prefieras
        numero_palabras = self.contar_palabras()
        tiempo_lectura = round(numero_palabras / palabras_por_minuto)
        return max(1, tiempo_lectura)  # Al menos 1 minuto de lectura

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)