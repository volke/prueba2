# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota_perdida', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota_perdida',
            name='datos_adicionales',
            field=models.TextField(default=1, max_length=500, verbose_name=b'Datos adicionales'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota_perdida',
            name='direccion',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota_perdida',
            name='sector',
            field=models.CharField(default=1, max_length=50, verbose_name=b'Sector'),
            preserve_default=False,
        ),
    ]
