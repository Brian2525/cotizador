from django.contrib import admin
from .models import Empresa

# Register your models here.


class EmpresaAdmin(admin.ModelAdmin): 
    list_display= ['id']
admin.site.register(Empresa, EmpresaAdmin)
