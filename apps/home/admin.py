# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *
from import_export.resources import ModelResource
from import_export.admin import *
# Register your models here.
class cash_reportResource(ModelResource):
    class Meta:
        model = cash_report

class cash_reportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =cash_reportResource
    list_display = ['id','cachier_id','amount','date']
class ChainResource(ModelResource):
    class Meta:
        model = Chain
class ChainAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =ChainResource
    list_display = ['id','chain_name','store_id','created_at']
class storeResource(ModelResource):
    class Meta:
        model = Store
class StoreAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =storeResource
    list_display = ['id','store_name','shop_owner_id','created_at']
 ######################################
class Payment_MethodsResource(ModelResource):
    class Meta:
        model = Payment_Methods
class Payment_MethodsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =Payment_MethodsResource
    list_display = ['id','name','created_at']
###############################################
class CachierResource(ModelResource):
    class Meta:
        model = Cachier
class CachierAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =CachierResource
    list_display = ['id','first_name','chain_id','created_at']
#################################################
class OrdersResource(ModelResource):
    class Meta:
        model = Orders
class OrdersAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class =OrdersResource
    list_display = ['id','cachier_id','payment_amount','created_at']   
@admin.register(Category_report)
class Category_reportAdmin(admin.ModelAdmin):
    list_display = ['id','category_id','amount','date']
    
admin.site.register(Category_Report_Per_Member)
admin.site.register(Cash_Report_Per_Member)
admin.site.register(cash_report,cash_reportAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Chain,ChainAdmin)
admin.site.register(Payment_Methods,Payment_MethodsAdmin)
admin.site.register(Cachier,CachierAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Suppliers)
admin.site.register(Coupon)
admin.site.register(Product_Item_Order)