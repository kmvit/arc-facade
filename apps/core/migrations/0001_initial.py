# Generated by Django 2.0.2 on 2018-02-26 09:44

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PageSkeleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('keywords', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1500)),
                ('is_active', models.BooleanField(default=False)),
                ('content', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('pageskeleton_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PageSkeleton')),
                ('image_1', models.ImageField(blank=True, upload_to='page')),
                ('image_2', models.ImageField(blank=True, upload_to='page')),
                ('image_3', models.ImageField(blank=True, upload_to='page')),
            ],
            bases=('core.pageskeleton',),
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('pageskeleton_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PageSkeleton')),
                ('image', models.ImageField(blank=True, upload_to='category_image')),
            ],
            bases=('core.pageskeleton',),
        ),
        migrations.CreateModel(
            name='ServiceSubcategory',
            fields=[
                ('pageskeleton_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PageSkeleton')),
                ('icon', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=False, to='core.ServiceCategory')),
            ],
            bases=('core.pageskeleton',),
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=False, to='core.ServiceSubcategory'),
        ),
    ]
