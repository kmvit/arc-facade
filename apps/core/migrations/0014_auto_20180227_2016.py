# Generated by Django 2.0.2 on 2018-02-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180227_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('home', 'home.html'), ('services', 'service.html'), ('page', 'page.html'), ('portfolio', 'portfolio.html'), ('contact', 'contact.html')], default='home', max_length=30),
        ),
    ]
