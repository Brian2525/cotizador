from django import forms 
from .models import Cliente


class ClienteForm(forms.ModelForm): 
    class Meta: 
        model=Cliente
        fields=['nombre_cliente', 'empresa_cliente', 'estado_pipeline', 'direccion_cliente', 'telefono_cliente', 'email_cliente']