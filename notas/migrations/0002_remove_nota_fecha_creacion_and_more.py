# Generated by Django 5.0.3 on 2024-04-03 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='fecha_publicacion',
        ),
    ]
