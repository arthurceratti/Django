# Generated by Django 3.0.8 on 2020-08-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_empresa_consumo_fora_ponta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='consumo_Fora_ponta',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='consumo_ponta',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='demanda_contratada',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='demanda_registrada',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='slug',
        ),
    ]
