from django import forms
from .models import Palestras


class PalestraForm(forms.ModelForm):
    class Meta:
        model = Palestras
        fields = '__all__'