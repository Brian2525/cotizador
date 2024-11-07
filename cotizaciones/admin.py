from django.contrib import admin
from .models import Check, Categoria, Status, Comentarios



class CheckAdmin(admin.ModelAdmin): 
    list_display= ('id','nombre_proyecto','cliente', 'numero_cotizacion')



admin.site.register(Check, CheckAdmin)
admin.site.register(Categoria)
admin.site.register(Status)
admin.site.register(Comentarios)
