# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_mascota_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(max_length=255, null=True, verbose_name=b'Descripcion', blank=True),
        ),
    ]
