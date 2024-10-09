from django.contrib import admin
from .models import Vendedor


class VendedorAdmin (admin.ModelAdmin): 
    list_display=('nombre')

admin.site.register(Vendedor)

# Register your models here.
