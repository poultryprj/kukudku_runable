from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Shop, Route
from .serializers import ShopSerializer

# View to list all routes and their shop counts
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Shop, Route
from .serializers import ShopSerializer

# View to list all routes and their shop counts
def route_list(request):
    try:
        # Retrieve all routes
        routes = Route.objects.all()

        # Create a list of dictionaries containing route IDs, names, and their respective shop counts
        route_data = []
        for route in routes:
            shops = Shop.objects.filter(route=route)
            shop_count = shops.count()
            route_data.append({'route_id': route.id, 'route_name': route.name, 'shop_count': shop_count})

        # Create a response containing route data
        response_data = {'routes': route_data}

        return JsonResponse(response_data)
    except Route.DoesNotExist:
        return JsonResponse({'error': 'Route not found'}, status=404)


# View to retrieve details of a specific route
# def route_detail(request, route_id):
#     # Attempt to retrieve the route by ID; return a 404 response if not found
#     route = get_object_or_404(Route, pk=route_id)

#     # Query shops for the specified route
#     shops = Shop.objects.filter(route=route)
#     shop_count = shops.count()

#     # Serialize the shop queryset
#     serializer = ShopSerializer(shops, many=True)

#     # Create a response containing the route name, shop count, and shop list
#     response_data = {
#         'route_name': route.name,
#         'shop_count': shop_count,
#         'shops': serializer.data
#     }

#     return JsonResponse(response_data)


def route_detail(request, route_id):
    # Attempt to retrieve the route by ID; return a 404 response if not found
    route = get_object_or_404(Route, pk=route_id)

    # Query shops for the specified route
    shops = Shop.objects.filter(route=route)
    shop_count = shops.count()

    # Serialize the shop queryset including the "outstanding_amount" field
    serializer = ShopSerializer(shops, many=True, context={'request': request})

    # Create a response containing the route name, shop count, and shop list
    response_data = {
        'route_name': route.name,
        'shop_count': shop_count,
        'shops': serializer.data
    }

    return JsonResponse(response_data)

