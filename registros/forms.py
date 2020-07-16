from django import forms
from registros.models import Erro

class ErroModelForm(forms.ModelForm):
    class Meta:
        model = Erro
        fields = ['level', 'descricao', 'origem', 'detalhes', 'producao', 'data', 'event']