# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota_perdida', '0003_auto_20151202_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota_perdida',
            name='perdido',
            field=models.BooleanField(default=1, verbose_name=b'Esta perdido?'),
            preserve_default=False,
        ),
    ]
