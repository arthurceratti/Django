# Generated by Django 3.0.8 on 2020-08-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='consumo_Fora_ponta',
            field=models.CharField(default='000', max_length=255),
        ),
    ]
