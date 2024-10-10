from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Check, Status, Comentarios
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
             }



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