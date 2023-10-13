# Create your views here.
from django.shortcuts import render

from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#from skipshop.models import skipModel
import json
#from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from dashboard.models import dashboardModel
from dashboard.serializers import dashboardSerializer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def dashboard_view(request):
    if request.method=='GET':
        users = dashboardModel.objects.filter() 
        dashboards_serializer = dashboardSerializer(users, many=True)
        data = dashboards_serializer.data
        data1 = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": data,
            }

        return JsonResponse(data1)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        cashierId = data.get('cashierid')
        routeId = data.get('routeid')
        
        dashboard_data = dashboardModel.objects.filter(cashierId='cashierid',routeId='routeid')
        dashboards_serializer = dashboardSerializer(users, many=True)