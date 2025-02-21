from django import forms
from biblioteca.models import Livro
from contas.models import Usuario

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"
        exclude = ["favoritos"]
