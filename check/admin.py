from django.contrib import admin
from .models import Check, Categoria, Status
# Register your models here.


class CheckAdmin(admin.ModelAdmin): 
    list_display= ('id', 'nombre_empresa', 'numero_cotizacion')



admin.site.register(Check, CheckAdmin)
admin.site.register(Categoria)
admin.site.register(Status)
