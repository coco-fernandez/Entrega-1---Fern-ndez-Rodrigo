from tabnanny import verbose
from django import forms

class nuevo_curso(forms.Form):
    nombre=forms.CharField(max_length=30)
    comision=forms.IntegerField(min_value=0)