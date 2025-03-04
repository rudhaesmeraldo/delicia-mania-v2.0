from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome_receita', 'tempo_preparo', 'rendimento', 'categoria', 'ingredientes', 'modo_preparo', 'imagem', 'data_receita']

