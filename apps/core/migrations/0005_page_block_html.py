# Generated by Django 2.0.2 on 2018-02-26 16:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='block_html',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
