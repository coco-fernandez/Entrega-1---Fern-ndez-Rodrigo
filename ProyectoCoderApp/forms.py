
from django import forms

class nuevo_curso(forms.Form):
    nombre=forms.CharField(max_length=30,label="Curso")
    comision=forms.IntegerField(min_value=0)