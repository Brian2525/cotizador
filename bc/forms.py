from django import forms
from .models import Vendedores



class VendedoresForm(forms.ModelForm):
    class Meta:
        model=Vendedores
    

        fields = [
                'nombre',
                'numero_contacto',
                'email',
                'facebook',
                'x_twitter',
                'instagram',
                'linkedin',
                'sitio_web',
                'video_corporativo',
            
            ]
            
            # Opcionalmente, puedes personalizar las etiquetas o widgets de los campos
        labels = {
                'x_twitter': 'X (Twitter)',
                'vendedores_relacionados': 'Vendedores Relacionados'
            }
            
        widgets = {
                'numero_contacto': forms.TextInput(attrs={'placeholder': 'Número de contacto'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
                'facebook': forms.URLInput(attrs={'placeholder': 'Enlace a tu perfil de Facebook'}),
                'x_twitter': forms.URLInput(attrs={'placeholder': 'Enlace a tu perfil en X (antes Twitter)'}),
                'instagram': forms.URLInput(attrs={'placeholder': 'Enlace a tu perfil de Instagram'}),
                'linkedin': forms.URLInput(attrs={'placeholder': 'Enlace a tu perfil de LinkedIn'}),
                'sitio_web': forms.URLInput(attrs={'placeholder': 'Enlace a tu sitio web'}),
                'video_corporativo': forms.URLInput(attrs={'placeholder': 'Enlace al video corporativo/personal'}),
                
            }
