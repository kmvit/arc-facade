from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import Http404
# Create your views here.

def home(request):
    page = get_object_or_404(Page, slug='index')
    service_list = Page.objects.filter(category__slug='service')
    banner_list = Banner.objects.all()
    context = {'service_list':service_list, 'page':page, 'banner_list': banner_list}
    return render (request, 'core/home.html', context)

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    service_list = Page.objects.filter(category__slug='service')
    decor_list = Page.objects.filter(category__slug='fasad-decor')
    portfolio_list = Portfolio.objects.all()
    context = {'page': page, 'service_list':service_list, 'portfolio_list':portfolio_list, 'decor_list':decor_list}
    return render(request, 'core/' + page.get_template_display(), context)
