from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import Http404
from apps.news.models import *
# Create your views here.

def home(request):
    page = get_object_or_404(Page, slug='index')
    service_list = Page.objects.filter(category__slug='service')
    banner_list = Banner.objects.all()
    news_list = News.objects.all()
    context = {'service_list':service_list, 'page':page, 'banner_list': banner_list, 'news_list': news_list}
    return render (request, 'core/home.html', context)

def sitemapview(request):
    return render(request, 'sitemap.xml', content_type="application/xhtml+xml")

def page(request, city_slug, slug):
    page = get_object_or_404(Page, slug=slug)
    city = get_object_or_404(City, slug=city_slug)
    path = request.path
    if city_slug:
        if city.slug in path:
            path = city.slug
    else:
        path = 'pyatigorsk'

    path = request.path
    service_list = Page.objects.filter(category__slug='service')
    decor_list = Page.objects.filter(category__slug='fasad-decor')
    portfolio_list = Portfolio.objects.all()
    adress = Adress.objects.get(city=city)
    context = {'page': page, 'service_list':service_list, 'portfolio_list':portfolio_list, 'decor_list':decor_list, 'path':path, 'city':city, 'adress':adress}
    return render(request, 'core/' + page.get_template_display(), context)

def page_detail(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    city = get_object_or_404(City, slug='pyatigorsk')
    url = page_slug
    service_list = Page.objects.filter(category__slug='service')
    decor_list = Page.objects.filter(category__slug='fasad-decor')
    portfolio_list = Portfolio.objects.all()
    adress = Adress.objects.get(city=city)
    context = {'page': page, 'service_list':service_list, 'portfolio_list':portfolio_list, 'decor_list':decor_list,'city':city,'adress':adress}
    return render(request, 'core/' + page.get_template_display(), context)
