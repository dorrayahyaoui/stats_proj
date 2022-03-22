from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics , status
from django.db.models import Count

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
            
            