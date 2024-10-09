from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Check, Status, Comentarios

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )



class CheckForm(forms.ModelForm):
    class Meta: 
        
    
        model = Check
        fields='__all__'


         # Etiqueta opcional para la opción vacía)

class ComentariosForm(forms.ModelForm):
    class Meta:
        model=Comentarios
        fields=[

            'resuelto',
            'comentario',
        ]