# Generated by Django 2.0.2 on 2018-04-09 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='born',
            field=models.DateField(default=datetime.datetime(2018, 4, 9, 19, 53, 49, 703275)),
        ),
    ]
