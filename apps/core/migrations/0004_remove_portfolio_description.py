# Generated by Django 2.0.2 on 2018-02-26 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
    ]
