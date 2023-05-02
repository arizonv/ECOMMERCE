from tkinter import Widget
from django import forms
from .models import contacto,Producto
import re
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ["nombre", "apellido", "email", "numero", "descripcion", "region", "comuna"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"cols": 37, "rows": 5}),
            "region": forms.Select(attrs={"id": "region"}),
            "comuna": forms.Select(attrs={"id": "comuna"}),
        }



class ProductoForm(forms.ModelForm):
    class Meta:

        model = Producto
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 37, 'rows': 5 }),
        }
        fields = '__all__'




class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        help_text='20 caracteres como máximo. Únicamente letras, números y @/./+/-/_'
    )
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text="La contraseña debe tener al menos 8 caracteres y no puede tener similitud a los demas campos."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text="Ingrese la misma contraseña de arriba, para su verificación."
    )

    class Meta:
        model = User
        fields = ["username" ,"first_name","last_name","email","password1","password2"]
        #fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^\w{1,20}$', username):
            raise forms.ValidationError('El nombre de usuario solo puede contener letras, números y @/./+/-/_ y debe tener una longitud máxima de 20 caracteres')
        return username






