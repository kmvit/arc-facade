# Generated by Django 2.0.2 on 2018-04-09 23:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
