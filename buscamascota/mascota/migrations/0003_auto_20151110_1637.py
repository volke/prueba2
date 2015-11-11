# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20151110_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='color',
            field=models.CharField(max_length=30, verbose_name=b'Color', blank=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(max_length=255, verbose_name=b'Descripcion', blank=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(max_length=30, verbose_name=b'Raza', blank=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(max_length=30, verbose_name=b'Sexo', blank=True),
        ),
    ]
