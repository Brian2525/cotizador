from django.contrib import admin
from .models import Deal


class DealAdmin (admin.ModelAdmin): 
    list_display=('nombre', 'value')

admin.site.register(Deal)

# Register your models here.
