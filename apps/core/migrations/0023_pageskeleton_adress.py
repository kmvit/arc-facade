# Generated by Django 2.0.2 on 2018-05-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_pageskeleton_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageskeleton',
            name='adress',
            field=models.CharField(default='Пятигорск, Бештаугорское шоссе', max_length=600),
        ),
    ]
