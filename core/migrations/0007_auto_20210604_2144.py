# Generated by Django 2.1.7 on 2021-06-05 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210604_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 6, 4, 21, 43, 57, 765662)),
        ),
    ]
