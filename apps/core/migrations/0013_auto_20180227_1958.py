# Generated by Django 2.0.2 on 2018-02-27 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180227_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='image_1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image_3',
        ),
    ]