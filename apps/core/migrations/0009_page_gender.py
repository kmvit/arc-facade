# Generated by Django 2.0.2 on 2018-02-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='gender',
            field=models.CharField(choices=[('home', 'home.html'), ('services', 'service.html'), ('page', 'page.html')], default='home', max_length=30),
        ),
    ]
