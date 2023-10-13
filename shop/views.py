from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from route.models import Routemodel
from shop.models import shopBalances, shopModel, shopOwners, shopRoutes
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@method_decorator(csrf_exempt, name='dispatch')
def shop_view(request):
    if request.method == 'GET':
        shoplist = shopModel.objects.all()
        
        shop_info = []
        for shop in shoplist:
            shop_info.append({
                'shopcode': shop.shopCode,
                'shopname': shop.shopName,
                'shoparea': shop.shopArea,
                'shopLatitude': shop.shopLatitude,
                'shoplongitude': shop.shopLongitude,
                'shopaddress': shop.shopAddress,
                'shoppincode': shop.shopPincode,
                'shopdistance': shop.shopDistance,
                'shopmobileno': shop.shopMobileNo,
                'shopalternateno': shop.shopAlternateNo,
                'shopownerid': shop.shopOwnerId,
                'shoptype': shop.shopType,
                'shopstatus': shop.shopStatus,
                'shopflexiblerate': shop.shopFlexibleRate,
            })
        
        if not shop_info:
            return JsonResponse({"message": "Shop Not Available In the List"}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'message_text': 'Success',
            'message_code': 1000,
            'message_data': shop_info
        }
    
        return JsonResponse(data, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
def shopowner_view(request):
    if request.method == 'GET':
        shopownerlist = shopOwners.objects.all()
        
        shop_owner = []
        for shopowner in shopownerlist:
            shop_owner.append({
                'ownername': shopowner.ownerName,
                'ownercontact': shopowner.ownerContactNo,
                'owneralternate': shopowner.ownerAlternateNo
            })
            
        if not shop_owner:
            return JsonResponse({"message": "Shop Owner Not Available In the List"}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'message_text': 'Success',
            'message_code': 1000,
            'message_data': shop_owner
        }
    
        return JsonResponse(data, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
def shoproute_view(request):
    if request.method == 'GET':
        shoproutelist = shopRoutes.objects.all()
        
        shop_route = []
        for shoproute in shoproutelist:
            shop_route.append({
                'shopid': shoproute.shopId,
                'routeid': shoproute.routeId,
                'shoporder': shoproute.shopOrder
            })
        
        if not shop_route:
            return JsonResponse({"message": "Shop Route Not Available In the List"}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'message_text': 'Success',
            'message_code': 1000,
            'message_data': shop_route
        }
    
        return JsonResponse(data, status=status.HTTP_200_OK)
    
    

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from route.models import Routemodel
from shop.models import shopModel, shopOwners, shopRoutes, shopBalances
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@method_decorator(csrf_exempt, name='dispatch')
def shopbalance_view(request):
    if request.method == 'GET':
        shopbalancelist = shopBalances.objects.all()
        
        shop_balance = []
        for shopbalance in shopbalancelist:
            shop_balance.append({
                'shopid': shopbalance.shopId,
                'shopbalance': shopbalance.shopBalance,  # Use the correct field name from your model
            })
        
        if not shop_balance:
            return JsonResponse({"message": "Shop Balance Not Available In the List"}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'message_text': 'Success',
            'message_code': 1000,
            'message_data': shop_balance
        }
    
        return JsonResponse(data, status=status.HTTP_200_OK)

