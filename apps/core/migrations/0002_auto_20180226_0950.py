# Generated by Django 2.0.2 on 2018-02-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageskeleton',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]