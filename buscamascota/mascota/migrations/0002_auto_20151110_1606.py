# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(max_length=255, verbose_name=b'descripcion', blank=True),
        ),
    ]
