from django.contrib import admin
from .models import Cliente, ContactForm

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre', 'empresa')
admin.site.register(Cliente)


def migrate_to_cliente(modeladmin, request, queryset):
    for contact in queryset:
        Cliente.objects.create(
            nombre=contact.nombre,
            empresa=contact.empresa,
            mail=contact.email,
            # Add other fields as necessary
        )
        contact.delete()
    modeladmin.message_user(request, "Selected contacts have been migrated to Clientes")

migrate_to_cliente.short_description = "Migrate selected contacts to Clientes"

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'email', 'fecha_creacion')
    readonly_fields = ('fecha_creacion',)
    actions = [migrate_to_cliente]

    def fecha_creacion(self, obj):
        return format_html('<span>{}</span>', obj.fecha_creacion)
    fecha_creacion.short_description = 'Fecha de Creación'

admin.site.register(ContactForm, ContactFormAdmin)
