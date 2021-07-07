from django import forms
from django.forms import ModelForm
from django.forms import widgets  #para definir los input del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Persona


class PersonaForm(forms.ModelForm):

    class Meta: 
        model= Persona
        fields = ['rut', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'contraseña']
        labels ={
            'rut': 'Ingrese su rut' ,
            'nombre': 'Nombre de Colaborador',
            'telefono': 'Telefono de Colaborador',
            'direccion': 'Direccion de Colaborador',
            'email': 'Email de Colaborador',
            'pais': 'Pais de Colaborador',
            'contraseña': 'Contraseña de Colaborador',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'XX.XXX.XXX-X', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
  
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email'
                    
                }
            ), 
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais'
                    
                }
            ), 
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contraseña'
                    
                }
            )
            
        }