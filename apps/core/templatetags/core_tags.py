# -*- coding: utf-8 -*-
from django import template
from apps.core.models import Page, Portfolio

register = template.Library()
@register.inclusion_tag('tags/menu_item.html', takes_context=True)
def menu_item(context):
    menu_list = Page.objects.filter(in_menu=True)
    context_dict = {'menu_list':menu_list}
    return context_dict

@register.inclusion_tag('tags/menu_item_footer.html', takes_context=True)
def menu_item_footer(context):
    menu_list = Page.objects.filter(category__slug='service')
    context_dict = {'menu_list':menu_list}
    return context_dict

@register.inclusion_tag('tags/last_in_portfolio.html',takes_context=True)
def last_in_portfolio(context):
    portfolio_list = Portfolio.objects.all()[:9]
    context_dict = {'portfolio_list':portfolio_list}
    return context_dict
    
@register.inclusion_tag('tags/portfolio_aside.html',takes_context=True)
def portfolio_aside(context):
    portfolio_list = Portfolio.objects.all()
    context_dict = {'portfolio_list':portfolio_list}
    return context_dict
