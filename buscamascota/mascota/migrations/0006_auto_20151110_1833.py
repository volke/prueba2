# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0005_auto_20151110_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='color',
            field=models.CharField(max_length=30, verbose_name=b'Color'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(max_length=30, verbose_name=b'Raza'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(max_length=30, verbose_name=b'Sexo'),
        ),
    ]
