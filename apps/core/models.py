from django.db import models
from autoslug import AutoSlugField
from tinymce import models as tinymce_models
from django.template.defaultfilters import slugify
# Create your models here.


class PageSkeleton(models.Model):
    """Base model for all models"""
    title = models.CharField(max_length=400)
    slug = models.SlugField(unique=True, blank=True)
    keywords = models.CharField(max_length=1000)
    description = models.CharField(max_length=1500)
    is_active = models.BooleanField(default=False)
    content = tinymce_models.HTMLField(blank=True)
    def __str__(self):
        return self.title



class Page(PageSkeleton):
    """Model for all Page"""
    category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='page', blank=True)
    block_html = tinymce_models.HTMLField(blank=True)
    block_html_2 = tinymce_models.HTMLField(blank=True)
    TEMPLATE_CHOICES = (
        ('home', 'home.html'),
        ('services', 'service.html'),
        ('decor_list', 'decor-list.html'),
        ('decor_detail', 'decor-detail.html'),
        ('page', 'page.html'),
        ('portfolio', 'portfolio.html'),
        ('contact', 'contact.html'),
    )
    template = models.CharField(max_length=30, choices=TEMPLATE_CHOICES, default='home')


class Portfolio(models.Model):
    """Model Portfolio"""
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=100, blank=True)
    CHOICES = (
        ('home', 'home'),
        ('building', 'building'),

    )
    category = models.CharField(max_length=30, choices=CHOICES, default='home')
    image = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.ImageField(upload_to='banner')
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.title
