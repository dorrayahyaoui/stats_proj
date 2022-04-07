# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.
class Cash_Report_Per_Member(models.Model):
    id = models.AutoField(primary_key=True)
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    is_member=models.BooleanField(db_index=True)
    receipts_quantity=models.IntegerField()
    product_quantity= models.IntegerField()   
class cash_report(models.Model):
    id = models.AutoField(primary_key=True)
    date=models.DateField(db_index=True)
    store_id=models.IntegerField(db_index=True)
    chain_id=models.IntegerField(db_index=True)
    cachier_id=models.IntegerField(db_index=True)
    member_data=models.ForeignKey(Cash_Report_Per_Member ,related_name='member_data',on_delete=models.CASCADE )
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    payment_method = models.IntegerField(db_index=True)
    product_quantity= models.IntegerField()
    receipts_quantity=models.IntegerField(default=0)
    return_quantity=models.IntegerField()
    coupon_quantity=models.IntegerField(default=0)
    coupon_amount=models.DecimalField(default=0,decimal_places=2,max_digits=12)
    return_receipts_quantity=models.IntegerField(default=0)
    refund_amount=models.DecimalField(decimal_places=2,max_digits=12,default=0)
    discount_amount=models.DecimalField(decimal_places=2,max_digits=12)    
class Category_Report_Per_Member(models.Model):
    id = models.AutoField(primary_key=True)
    amount=models.DecimalField(decimal_places=2,max_digits=12)
    is_member=models.BooleanField(db_index=True)
    receipts_quantity=models.IntegerField()
    product_quantity= models.IntegerField()    
class Category_report(models.Model):
    id = models.AutoField(primary_key=True)
    date=models.DateField(db_index=True)
    store_id=models.IntegerField(db_index=True)
    chain_id=models.IntegerField(db_index=True)
    category_id=models.IntegerField(db_index=True)
    member_data=models.ForeignKey(Category_Report_Per_Member ,related_name='member_data',on_delete=models.CASCADE )
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    payment_method = models.IntegerField(db_index=True)
    product_quantity= models.IntegerField()
    receipts_quantity=models.IntegerField(default=0)
    return_quantity=models.IntegerField()
    coupon_quantity=models.IntegerField(default=0)
    coupon_amount=models.DecimalField(decimal_places=2,max_digits=12,default=0)
    return_receipts_quantity=models.IntegerField(default=0)
    refund_amount=models.DecimalField(decimal_places=2,max_digits=12,default=0)
    discount_amount=models.DecimalField(decimal_places=2,max_digits=12)
class Store(models.Model):
    id=models.AutoField(primary_key=True)
    store_name=models.CharField(max_length=500)
    store_name_en=models.CharField(max_length=500,null=True)
    store_name_it=models.CharField(max_length=500,null=True)
    store_area=models.CharField(max_length=500,null=True)
    store_domain=models.CharField(max_length=500,null=True)
    store_grade_id=models.IntegerField(null=True)
    store_logo=models.CharField(max_length=500,null=True)
    store_adress =models.CharField(max_length=500,null=True)
    contact =models.CharField(max_length=500,null=True)
    store_longitude=models.CharField(max_length=500,null=True)
    store_latitude =models.CharField(max_length=500,null=True)
    opening_hour=models.CharField(max_length=500,null=True)
    closure_hour=models.CharField(max_length=500,null=True)
    store_ip =models.CharField(max_length=500,null=True)
    store_is_open=models.IntegerField(null=True)
    store_is_selfsupport =models.IntegerField(null=True)
    shop_owner_id=models.IntegerField(unique=True,db_index=True)
    created_at =models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
    deleted_at =models.DateTimeField(default=timezone.now,null=True)
    tax_number = models.CharField(max_length=500,null=True)
    company_id =models.IntegerField(null=True)
class Chain(models.Model):
    id=models.AutoField(primary_key=True)
    store_id=models.IntegerField(db_index=True)
    chain_name=models.CharField(max_length=500,null=True)
    adress=models.CharField(max_length=500,null=True)
    chain_mobile=models.CharField(max_length=500,null=True)
    chain_telephone=models.CharField(max_length=500,null=True)
    chain_opening_hours=models.CharField(max_length=500,null=True)
    chain_close_hours=models.CharField(max_length=500,null=True)
    chain_trafic_line=models.CharField(max_length=500,null=True)
    chain_img=models.CharField(max_length=500,null=True)
    chain_lng=models.CharField(max_length=500,null=True)
    chain_lat=models.CharField(max_length=500,null=True)
    approved=models.CharField(max_length=500,null=True)
    fattura_format=models.CharField(max_length=500,null=True)
    next_format_num=models.IntegerField(null=True)
    chain_ip =models.CharField(max_length=500,null=True)
    chain_district_id=models.IntegerField(null=True,db_index=True)
    chain_district_info =models.CharField(max_length=500,null=True)
    shop_owner_id =models.IntegerField(db_index=True)
    manager_id=models.IntegerField(null=True,db_index=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at =models.DateTimeField(default=timezone.now)
    deleted_at =models.DateTimeField(default=timezone.now,null=True)
    cash_registers =models.IntegerField(null=True)
    contact =models.CharField(max_length=500,null=True)
    warehouse_id =models.IntegerField(null=True,db_index=True)
    manager2_id =models.IntegerField(null=True)
    manager3_id = models.IntegerField(null=True)
    chain_code =models.CharField(max_length=500,null=True)
    address =models.CharField(max_length=500,null=True)
    zip_code =models.CharField(max_length=500,null=True)
    city =models.CharField(max_length=500,null=True)
    state_province =models.CharField(max_length=500,null=True)
    country =models.CharField(max_length=500,null=True)
    tax_number =models.CharField(max_length=500,null=True)
    company_id=models.IntegerField(null=True,db_index=True)
    has_member_point=models.IntegerField(null=True)
    is_online =models.IntegerField(null=True)
    all_products_online =models.IntegerField(null=True)
class Payment_Methods(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
class Cachier(models.Model) :
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500)
    store_id =models.IntegerField(null=True,db_index=True)
    chain_id =models.IntegerField(null=True,db_index=True)
    contact=models.CharField(max_length=500,null=True)
    password=models.CharField(max_length=500,null=True)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)
    img_url=models.CharField(max_length=500,null=True)
    img_name =models.CharField(max_length=500,null=True)
    hidden = models.IntegerField(default=1)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
    user_id=models.IntegerField(default=1)
    
    

class Orders(models.Model):
    id=models.AutoField(primary_key=True)
    payment_amount= models.DecimalField(decimal_places=2,max_digits=12,null=True)
    member_price=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    TVA=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    chain_id =models.IntegerField(db_index=True)
    cachier_id=models.IntegerField(db_index=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=timezone.now)
    payment_method_id=models.IntegerField(db_index=True)
    discount_amount=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    order_number = models.CharField(max_length=500,null=True)
    card_number=models.IntegerField(db_index=True)
    vip_point=models.IntegerField(db_index=True)
    cart_data = models.TextField(max_length=500,null=True)
    invoice =models.CharField(max_length=500,null=True)
    order_payment_amount = models.DecimalField(decimal_places=2,max_digits=12,null=True)
    product_quantity = models.IntegerField(null=True)
    store_id =models.IntegerField(db_index=True)
    operator=models.CharField(max_length=500,null=True)
    order_cost=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    online_order_number = models.CharField(max_length=500,null=True)
    online_user_id =models.CharField(max_length=500,null=True)
    payment_date=models.DateTimeField(default=timezone.now)
    is_paid =models.IntegerField()
    
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category_name =models.CharField(max_length=500,null=True)
    category_it =models.CharField(max_length=500,null=True)
    category_cn =models.CharField(max_length=500,null=True)
    category_fr =models.CharField(max_length=500,null=True)
    parent_category_id=models.IntegerField(db_index=True)
    deleted_at =models.DateTimeField(default=timezone.now,null=True)
    img_url=models.CharField(max_length=500,null=True)
    img_name=models.CharField(max_length=500,null=True)
    tax =models.DecimalField(decimal_places=2,max_digits=10)
    has_user=models.IntegerField(null=True)
    category_order=models.IntegerField(null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)
    deleted_at=models.DateTimeField(default=timezone.now)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    chain_id = models.IntegerField(db_index=True)
    inbound_return_stock = models.IntegerField(null=True)
    product_weight = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    outbound_return_stock = models.IntegerField(null=True)
    discount_price = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    member_point = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    is_hidden = models.BooleanField(null=True)
    shop_owner_id =models.IntegerField(null=True,db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    member_price = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    product_quantity = models.IntegerField(null=True)
    tax_rate = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    range_id = models.CharField(max_length=100,null=True)
    warn_quantity = models.IntegerField(null=True,db_index=True)
    category_id = models.IntegerField(null=True,db_index=True)
    updated_at = models.DateTimeField(default=timezone.now)
    img_name = models.CharField(max_length=100,null=True)
    product_description = models.CharField(max_length=100,null=True)
    cost_price = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    member_privilege = models.IntegerField(db_index=True,null=True)
    updated_return_date = models.DateTimeField(default=timezone.now)
    max_warn_quantity = models.IntegerField(db_index=True,null=True)
    product_barcode = models.CharField(max_length=100,null=True)
    product_size = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    product_color = models.DecimalField(decimal_places=2,max_digits=12,default=0)
    unit_price = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    deleted_at = models.DateTimeField(default=timezone.now)
    product_name = models.CharField(max_length=100,null=True)
    item_return = models.IntegerField(null=True)
    expired_date = models.DateTimeField(default=timezone.now)
    shop_id = models.IntegerField(db_index=True,null=True)
    img_url = models.CharField(max_length=100,null=True)
    supplier_id = models.IntegerField(db_index=True,null=True)
    return_date = models.DateTimeField(default=timezone.now)
    
class Product_Item_Order(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField(db_index=True,null=True)
    order_item_return =models.IntegerField(null=True)
    chain_id = models.IntegerField(null=True)
    item_id = models.IntegerField(null=True,db_index=True)
    order_item_amount = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    item_unit_price = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    created_at = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    order_item_quantity = models.CharField(max_length=100)
    item_rate = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    category_id = models.IntegerField(db_index=True,null=True)
    updated_at = models.CharField(max_length=100)
    product_id = models.IntegerField(null=True,db_index=True)
    order_id = models.IntegerField(db_index=True,null=True)
    order_item_payment_amount =models.DecimalField(decimal_places=2,max_digits=10,default=0)

    
class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True,db_index=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    img_name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    shop_owner_id = models.IntegerField(blank=True, null=True,db_index=True)
 
    
class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField(db_index=True)
    chain_id =models.IntegerField(db_index=True)
    barcode = models.CharField(max_length=255)
    start_date = models.IntegerField(db_index=True)
    expire_date = models.IntegerField(db_index=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    used = models.IntegerField(db_index=True)
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField(db_index=True)
    sales=models.DecimalField(decimal_places=2,max_digits=12)
    amount_per_card=models.DecimalField(decimal_places=2,max_digits=12)
    amount_cash =models.DecimalField(decimal_places=2,max_digits=12)
    products_sold= models.IntegerField()  
    total_order= models.IntegerField()  
    sales_member =models.DecimalField(decimal_places=2,max_digits=12)
    sales_non_member =models.DecimalField(decimal_places=2,max_digits=12)
    products_member= models.IntegerField()  
    products_non_member=models.IntegerField()  
    date=models.DateField(db_index=True)





