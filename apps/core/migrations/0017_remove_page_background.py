# Generated by Django 2.0.2 on 2018-03-05 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_page_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='background',
        ),
    ]
