from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
import json
from route.models import Routemodel
from shoplist.models import shoplistModel
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from shoplist.serializers import ShopListSerializer


@method_decorator(csrf_exempt, name='dispatch')

def shoplist_view(request):
    if request.method == 'GET':
    #data = json.loads(request.body.decode("utf-8"))
        shoplist = shoplistModel.objects.filter()

        shop_list = []
        for shop in shoplist:
            shop_list.append({
                'shopcode': shop.shopCode,
                'shopname': shop.shopname,
            })
        
        data = {
            'message_text': 'Success',
            'message_code':1000,
            'message_data': shop_list    
        }
    
        if shop_list == '':
            return JsonResponse(data="Shop Not Available In the List")
    
        return JsonResponse(data , status=200)

    # def post(self):
    #     shopcode = data.get('shopcode')
    #     shopname = data.get('shopname')
    #     shoplist = shopModel.objects.all()

        
    #     if not shopcode or shopcode.strip() == "":
    #         return JsonResponse({"error": "Shopcode cannot be blank, zero, or whitespace."} , status=status.HTTP_400_BAD_REQUEST)
        
    #     if not shopname or shopname.strip() == "":
    #         return JsonResponse({"error": "Shopname cannot be blank, zero, or whitespace."} , status=status.HTTP_400_BAD_REQUEST)
        
        
    #     if shopcode == shoplist.get("shopcoder") and shopname == shoplist.get("shopname"):
    #         data = {
                
    #                 "message_text": "Shop added successfully",
    #                 "message_code": 1000,
    #                 "message_data": shoplist,
    #             }
        