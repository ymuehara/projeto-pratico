# Generated by Django 3.0.8 on 2020-07-19 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_log_detalhes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='ambiente',
            field=models.CharField(blank=True, choices=[('Homologação', 'Homologação'), ('Dev', 'Dev'), ('Produção', 'Produção')], max_length=15, verbose_name='Ambiente'),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
