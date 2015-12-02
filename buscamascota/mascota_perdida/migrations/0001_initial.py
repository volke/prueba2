# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota_perdida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo')),
                ('raza', models.CharField(max_length=50, verbose_name=b'Raza')),
                ('color', models.CharField(max_length=50, verbose_name=b'Color')),
                ('sexo', models.CharField(max_length=50, verbose_name=b'Sexo')),
                ('foto', models.FileField(upload_to=b'', verbose_name=b'Foto')),
            ],
        ),
    ]
