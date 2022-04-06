# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.home import api
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/cachier/monthly',api.monthly_orders_per_cachier.as_view(),name='sales per month '),
    # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls"))             # UI Kits Html files
]
