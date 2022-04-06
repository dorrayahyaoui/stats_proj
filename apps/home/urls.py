# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from . import api

urlpatterns = [

    # The home page
    path('apex/',views.stats_tuto,name='tuto statts charts '),
    path('', views.index, name='home'),
    path ('api/cachier/monthly',api.monthly_orders_per_cachier.as_view(),name='sales per month '),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
