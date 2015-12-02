# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='caza_recompenza',
            field=models.BooleanField(default=1, verbose_name=b'caza_recompenza'),
            preserve_default=False,
        ),
    ]
