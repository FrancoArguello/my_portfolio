from django import forms
import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    # expresion regular que valida que comienze opcional con el signo + y solo acepte numeros y debe ingresar un minimo de 10 num y maximo 15
    phone_regex = re.compile(r'^\+?[0-9]{10,15}$')
    if not phone_regex.match(value):
        raise ValidationError(
            'Por favor ingrese un número de teléfono válido.')


class ContactForm(forms.Form):

    fullname = forms.CharField(required=True, min_length=5, max_length=50, widget=forms.TextInput(
        attrs={'class': 'input-contact', 'placeholder': 'Ingresu su nombre y apellido'}))

    email = forms.EmailField(
        required=True, min_length=1, max_length=50, widget=forms.EmailInput(attrs={'class': 'input-contact', 'placeholder': 'Ingrese su email'}))

    phone = forms.CharField(
                            required=True, validators=[validate_phone_number], widget=forms.TextInput(attrs={'class': 'input-contact', 'placeholder': 'Ingrese su teléfono +54 11 xxxxxxxx'}))

    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'id' : 'text-area', 'class': 'input-contact', 'placeholder': 'Ingresu aquí su mensaje...', 'cols': '70',  'rows': '10'}))
