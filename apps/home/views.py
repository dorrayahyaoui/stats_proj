# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from django.db.models import Count

@login_required(login_url="/login/")
def index(request):
    query=Orders.objects.filter(cachier_id=11).values('created_at__date').annotate(count=Count('id')).values('created_at__date', 'count').order_by('created_at__date')
    query1=Orders.objects.filter(cachier_id=11).extra({'month':"Extract(month from created_at)"}).values_list('month').annotate(Count('id'))
    query2= Orders.objects.filter(cachier_id=11,created_at__month=12).extra({'day':"Extract(day from created_at)"}).values_list('day').annotate(Count('id'))
    print('******************************************')
    print(list(query1))
    print('******************************************')
    print('******************************************')
    print(list(query2))
    context = {'sales':query1 }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     query=Orders.objects.filter(cachier_id=1).values('created_at__date').annotate(count=Count('id')).values('created_at__date', 'count').order_by('created_at__date')
#     context = {'sales':query }
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))


