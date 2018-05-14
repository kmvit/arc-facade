from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *
# Create your views here.

class NewsList(ListView):
    model = News
    
class NewsDetail(DetailView):
    model = News