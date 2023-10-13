from django.shortcuts import render

#Create your views here.
from django.shortcuts import render

#
from django.views import View
from django.http import JsonResponse
import json
from route.models import Routemodel
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from shoplist.models import shoplistModel

@method_decorator(csrf_exempt, name='dispatch')

    # def get(self, request,format=None):

    #     data = json.loads(request.body.decode("utf-8"))
        # r_id = data.get('Route Title')
        # r_info = data.get('Route Info')
        

    #     product_data = {
    #         'Route Title': r_id,
    #         'Route Info': r_info,
            
    #     }

    #     user_id = Routemodel.objects.get(**product_data)

    #     data = {
    #         "routestatus":[{
    #         "message_text": f"Route selected successfully",
    #         "status_code" : f"1000_OK"
    #     }]
    #     }
    #     return JsonResponse(data,user_id, status=200)
    
    
def route_view(request):
    #data = json.loads(request.body.decode("utf-8"))
    if request.method == 'GET':
    
        routes = Routemodel.objects.filter()
        # r_id = data.get('Route Title')
        # r_info = data.get('Route Info')
        

        route_data = []
        for route in routes:
            route_data.append({
                'route_title': route.RouteId,
                'route_name': route.RouteName,
                'route_startpoint': route.RouteStartPoint,
                'route_endpoint' : route.RouteEndPoint,
                'route_areas' : route.RouteAreas
            })

        
        # def select_object(route_data, route_id):
        #     for object in route_data:
        #         if object["route_title"] == route_id:
        #             return object
        #     return None


        # object = select_object(route_data, 2)
        # if object:
        #     print(object["name"])
        # else:
        #     print("Object not found.")
        
    #     def select_route_by_title(route_data, route_title):
    #         for route in route_data:
    #             if route["route_title"] == route_title:
    #                 return route
    #         return None

    # # Example usage: Select route with route_title = 'Sample Route'
    #     selected_route = select_route_by_title(route_data, 'Sample Route')
    #     if selected_route:
    #         print(selected_route["route_title"])
    #     else:
    #         print("Route not found.")
        
        data = {
            'message': 'Success',
            'message_code':1000,
            'message_data': route_data,
        }

    
        if routes == '':
            data = {
                'message': 'Failure',
                'message_code':999,
                'message_data': {},
        }
        return JsonResponse(data)

    return JsonResponse(data, status=status.HTTP_200_OK)

        
    
    
