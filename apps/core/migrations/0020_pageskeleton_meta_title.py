# Generated by Django 2.0.2 on 2018-03-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180313_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageskeleton',
            name='meta_title',
            field=models.CharField(default='Поменять title страницы', max_length=350),
        ),
    ]
