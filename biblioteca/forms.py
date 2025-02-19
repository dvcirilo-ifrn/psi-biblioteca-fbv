from django import forms
from .models import Livro

class GeneroForm(forms.Form):
    generos = forms.ChoiceField(choices=Livro.GENEROS)
