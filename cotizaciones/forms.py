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
        fields=[
            'nombre_gerente',
            'numero_cotizacion',
            'fecha_solicitud',
            'nombre_proyecto',
            'volumen_estimado',
            'producto_nuevo', 
            'numero_tintas',
            'tipo_producto',
            'tecnologia_fabricacion',
            'nombre_empresa',
             'motivo_rechazo',     
                'lugar_entrega',
                'precio_objetivo',  'comentarios_adicionales'
                , 'frecuencia_compra', 'categoria' ]


        widgets={
            'numero_cotizacion': forms.NumberInput(attrs={'class': 'mb-3 form-control', 'placeholder': 'Numero de cotizacion'}),
            'fecha_solicitud': forms.DateInput(attrs={'class': 'form-control','type':'date',  'placeholder': 'Enter title'}),
            'nombre_proyecto' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'tecnologia_fabricacion': forms.Select(choices=CATEGORY_CHOICES,attrs={'class': 'form-select' } ),

        }

         # Etiqueta opcional para la opción vacía)


class UpdateStatus(forms.ModelForm):
    model=Check
    fields=['estatus']
