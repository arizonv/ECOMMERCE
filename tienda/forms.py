from tkinter import Widget
from django import forms
from .models import contacto,Producto

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User


class ContactoForm (forms.ModelForm):
    class Meta:
        model = contacto
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 37, 'rows': 5 }),
        }
        fields = ["nombre" ,"apellido","email" ,"numero","descripcion",'region', 'comuna']


class ProductoForm(forms.ModelForm):
    class Meta:

        model = Producto
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 37, 'rows': 5 }),
        }
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username" ,"first_name","last_name","email","password1","password2"]
        #fields = '__all__'





