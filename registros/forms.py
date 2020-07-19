from django import forms
from registros.models import Log

class LogModelForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['level', 'descricao', 'origem', 'detalhes', 'ambiente', 'data', 'event']