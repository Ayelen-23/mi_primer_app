# Generated by Django 5.2.3 on 2025-07-08 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_primer_app', '0002_alter_pais_idioma_oficial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='idioma_oficial',
        ),
    ]
