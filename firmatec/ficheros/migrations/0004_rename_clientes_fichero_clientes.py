# Generated by Django 3.2.3 on 2021-09-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficheros', '0003_fichero_clientes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichero',
            old_name='Clientes',
            new_name='clientes',
        ),
    ]
