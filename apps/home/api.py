from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics , status
from django.db.models import Count
from django.core import serializers
from django.db.models import Sum
class monthly_orders_per_cachier(APIView):
    def get(self,request):
        response_content = {'error': 'Send POST request!!'}
        return Response(response_content,status='405')
    def post(self, request, *args, **kwargs):
        if 'ID' not in  request.data:
            response_content = {'error': 'Provide a cachier ID!!'}
            return Response(response_content, status='400')
        try:
            query=Orders.objects.filter(cachier_id=11).values('created_at__date').annotate(count=Count('id')).values('created_at__date', 'count').order_by('created_at__date')
            query1=Orders.objects.filter(cachier_id=11).extra({'month':"Extract(month from created_at)"}).values_list('month').annotate(Count('id'))
            query2= Orders.objects.filter(cachier_id=11,created_at__month=12).extra({'day':"Extract(day from created_at)"}).values_list('day').annotate(Count('id'))
            print('******************************************')
            l1=list(query)
            print(list(query))
            print('******************************************')
            l2=list(query1)
            print(list(query1))
            print('******************************************')
            l3=list(query2)
            print(list(query2))
            response_content={'list1':l1,'list2':l2,'list3':l3}
            return Response(response_content,status=404)
        except Exception as e :
            response_content={'error':str(e)}
            return Response(response_content,status=404)
            
class stat_per_cashier_id(APIView):
    def get(self,request):
        response_content = {'error': 'Send POST request!!'}
        return Response(response_content,status='405')
    def post(self, request, *args, **kwargs):
        if 'ID' not in  request.data:
            response_content = {'error': 'Provide a cachier ID!!'}
            return Response(response_content, status='400')
        try:
            query=cash_report.objects.filter(id=11).extra({'month':"Extract(month from date)"}).values_list('month').annotate(Count('id'))
            l1=list(query)
            response_content={'list1':l1}
            return Response(response_content,status=200)
        except Exception as e :
            response_content={'error':str(e)}
            return Response(response_content,status=404)
# class stat_cashier_bystore(APIView):
#     def get(self,request):
#         response_content = {'error': 'Send POST request!!'}
#         return Response(response_content,status='405')
#     def post(self, request, *args, **kwargs):
#         if 'Store_ID' not in  request.data:
#             response_content = {'error': 'Provide a Store_ID !!'}
#             return Response(response_content, status='400')
#         try:
#             qs=cash_report.objects.filter(store_id=request.data['Store_ID'],date=request.data['date'])
#             toal_cash=qs.filter(payment_method=1).aggregate(TOTAL = Sum('amount'))['TOTAL']
#             total_debit=qs.filter(payment_method=2).aggregate(TOTAL = Sum('amount'))['TOTAL']
#             total_amount=qs.aggregate(TOTAL = Sum('amount'))['TOTAL']
#             product_quantity=qs.aggregate(Total_Products = Sum('product_quantity'))['Total_Products']
#             product_quantity_cash=qs.filter(payment_method=1).aggregate(Total_Product_Cash = Sum('product_quantity'))['Total_Product_Cash']
#             product_quantity_debit=qs.filter(payment_method=2).aggregate(Total_Product_Debit = Sum('product_quantity'))['Total_Product_Debit']
#             total_discount=qs.aggregate(Total_Discount = Sum('discount_amount'))['Total_Discount']
#             total_refund=qs.aggregate(Total_Refund = Sum('refund_amount'))['Total_Refund']        
#             response_content={'toal_cash':toal_cash,'total_debit':total_debit,'total_amount':total_amount,'product_quantity':product_quantity,'product_quantity_cash':product_quantity_cash,'product_quantity_debit':product_quantity_debit,'total_discount':total_discount,'total_refund':total_refund}
#             return Response(response_content,status=200)
#         except Exception as e :
#             response_content={'error':str(e)}
#             return Response(response_content,status=404)
#             

class stat_cashier_bystore(APIView):
    def get(self,request):
        response_content = {'error': 'Send POST request!!'}
        return Response(response_content,status='405')
    def post(self, request, *args, **kwargs):
        if 'Store_ID' not in  request.data:
            response_content = {'error': 'Provide a Store_ID !!'}
            return Response(response_content, status='400')
        try:
            qs=cash_report.objects.filter(store_id=request.data['Store_ID'],date=request.data['date']).group_by(cachier_id)
            
           
            response_content={'result':list(qs)}
            return Response(response_content,status=200)
        except Exception as e :
            response_content={'error':str(e)}
            return Response(response_content,status=404)