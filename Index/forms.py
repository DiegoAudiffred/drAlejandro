from django import forms
from db.models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'phone_number', 'email', 'descripción']
        labels = {
            'name': 'Nombre',
            'phone_number': 'Teléfono',
            'email': 'Correo electrónico',
            'descripción': 'Descripción',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingresa tu nombre'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu teléfono'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu correo electrónico'
            }),
            'descripción': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje',
                'rows': 4
            }),
        }
