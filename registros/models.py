from django.db import models
import datetime

# Create your models here.
LEVEL_CHOICES = [('critical', 'critical'),
                 ('debug', 'debug'),
                 ('error', 'error'),
                 ('warning', 'warning'),
                 ('information', 'information')]

class Log(models.Model):

    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, blank=True)
    event = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField('Descrição', blank=True)
    detalhes = models.TextField('Detalhes', blank=True)
    ambiente = models.CharField('Ambiente', max_length=15, choices=[('Homologacao', 'Homologacao'), ('Dev', 'Dev'), ('Produção', 'Produção')], blank=True)

    def __str__(self):
        return self.level

