# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raza', models.CharField(max_length=30, verbose_name=b'raza', blank=True)),
                ('color', models.CharField(max_length=30, verbose_name=b'color', blank=True)),
                ('sexo', models.CharField(max_length=30, verbose_name=b'sexo', blank=True)),
                ('descripcion', models.CharField(max_length=255, verbose_name=b'descripcion', blank=True)),
            ],
        ),
    ]
