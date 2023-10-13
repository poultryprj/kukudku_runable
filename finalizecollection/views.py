from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status
from django.http import JsonResponse
from finalizecollection.serializers import finalizecollectionSerializer

@method_decorator(csrf_exempt, name='dispatch')
def finalize_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        cashierId = data.get('cashierid')
        routeId = data.get('routeid')
        
        if cashierId is not None and routeId is not None:
            product_data = {
                'cashierId': cashierId,  # Note the capital 'I'
                'routeId': routeId,      # Note the capital 'I'
    }

            # Create the serializer instance with the provided data
            serializer = finalizecollectionSerializer(data=product_data)
            
            if serializer.is_valid():
                serializer.save()
                
                response_data = {
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": product_data,
                }
                return JsonResponse(response_data, status=status.HTTP_200_OK)
            else:
                error_data = {
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": {},
                }
                return JsonResponse(error_data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {
                "message_text": "Failure",
                "message_code": 999,
                "message_data": {},
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
