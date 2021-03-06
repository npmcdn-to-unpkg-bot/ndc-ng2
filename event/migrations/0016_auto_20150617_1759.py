# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_default_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='default_rate',
            name='rate',
            field=models.IntegerField(unique=True, choices=[(0, b'Member dance only'), (1, b'Member lesson and dance'), (2, b'Non-member dance only'), (3, b'Non-member lesson and dance'), (4, b'Tips for blues'), (5, b'UC Santa Cruz student'), (6, b'Exempt'), (7, b'DJ / Instructor'), (8, b'Volunteer')]),
            preserve_default=True,
        ),
    ]
