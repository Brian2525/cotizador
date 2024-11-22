from django.contrib import admin
from .models import PerfilUsuario, Categoria, Tag, Post

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'presentacion')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion')
    list_filter = ('categoria', 'tags', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')

