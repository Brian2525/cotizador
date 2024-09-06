from django.contrib import admin
from .models import Vendedores 





class VendedoresAdmin(admin.ModelAdmin): 
    list_display= ('id', 'nombre', 'email')
    

admin.site.register(Vendedores, VendedoresAdmin)

# Register your models here.
