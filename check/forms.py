# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Check, Status

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class CheckForm(forms.ModelForm):
    class Meta: 
        CATEGORY_CHOICES= [('Termoencogible', 'Termoencogible'), ('Impresion digital', 'Impresion digital')]
        #CATEGORY_CHOICES= Categoria.objects.all()
        model = Check
        fields=['numero_cotizacion','nombre_gerente','nombre_cliente','nombre_proyecto','volumen_estimado', 'numero_tintas', 'tecnologia_fabricacion', 'lugar_entrega', 'estatus',  'producto_nuevo','fecha_solicitud', 'precio_objetivo', 'tipo_producto', 'comentarios_adicionales', 'frecuencia_compra','autor' ]

        widgets={
            'nombre_gerente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'fecha_solicitud': forms.DateInput(attrs={'class': 'form-control','type':'date',  'placeholder': 'Enter title'}),
            'tecnologia_fabricacion': forms.Select(choices=CATEGORY_CHOICES),

        }

         # Etiqueta opcional para la opción vacía)

    #estatus=forms.ModelChoiceField(
    #    queryset=Status.objects.all(),
    #    widget=forms.Select(attrs={'class': 'form-control'}),
    #    empty_label="Select a category"  # Etiqueta opcional para la opción vacía)
    #)

