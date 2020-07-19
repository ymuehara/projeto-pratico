from rest_framework import serializers
from .models import Log

class LogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'level', 'event', 'data', 'origem', 'descricao', 'detalhes', 'ambiente']
