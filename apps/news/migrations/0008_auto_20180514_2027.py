# Generated by Django 2.0.2 on 2018-05-14 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180514_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='born',
            field=models.DateField(default=datetime.datetime(2018, 5, 14, 20, 27, 32, 908827)),
        ),
    ]
