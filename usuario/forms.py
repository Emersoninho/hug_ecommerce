from django import forms
from.models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email','senha')