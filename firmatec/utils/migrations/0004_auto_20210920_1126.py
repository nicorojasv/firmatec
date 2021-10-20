# Generated by Django 3.2.3 on 2021-09-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_auto_20210920_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='representante_legal',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='rut_representante',
        ),
        migrations.AddField(
            model_name='planta',
            name='representante_legal',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='planta',
            name='rut_representante',
            field=models.CharField(blank=True, error_messages={'unique': 'Ya existe un representante legal con este RUT registrado.'}, max_length=12, null=True, unique=True),
        ),
    ]
