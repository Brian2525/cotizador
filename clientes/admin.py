from django.contrib import admin
from .models import Cliente

# Register your models here.




class ClienteAdmin(admin.ModelAdmin): 
    list_display= ('nombre_cliente', 'empresa_cliente')
    

admin.site.register(Cliente, ClienteAdmin)
