# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota_perdida', '0002_auto_20151202_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota_perdida',
            name='foto',
            field=models.FileField(upload_to=b'', verbose_name=b'Foto', blank=True),
        ),
    ]
