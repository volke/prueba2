# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20151110_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name=b'Nombre', blank=True),
        ),
    ]
