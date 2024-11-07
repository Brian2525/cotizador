from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre', 'empresa')
admin.site.register(Cliente)