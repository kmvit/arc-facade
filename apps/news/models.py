from django.db import models
from tinymce import models as tinymce_models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='news')
    content = tinymce_models.HTMLField()
    born = models.DateField(default=datetime.datetime.today())
    
    def __str__(self):
        return self.title