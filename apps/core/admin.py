from django.contrib import admin
from .models import *
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    
admin.site.register(Page, PageAdmin)
admin.site.register(Portfolio)
admin.site.register(Banner)
