from django import forms
from .models import Palestras, Comentarios


class PalestraForm(forms.ModelForm):
    class Meta:
        model = Palestras
        exclude = ['data_criacao','user']

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['texto']