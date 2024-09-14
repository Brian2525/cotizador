from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Check, Categoria, Status



class CheckAdmin(ModelAdmin): 
    list_display= ('id', 'nombre_empresa', 'numero_cotizacion')



admin.site.register(Check, CheckAdmin)
admin.site.register(Categoria)
admin.site.register(Status)
