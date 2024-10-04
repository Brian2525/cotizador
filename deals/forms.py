from django import forms
from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'description', 'value', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Deal'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Deal', 'rows': 3}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }