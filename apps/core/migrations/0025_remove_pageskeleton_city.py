# Generated by Django 2.0.2 on 2018-05-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20180514_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageskeleton',
            name='city',
        ),
    ]
