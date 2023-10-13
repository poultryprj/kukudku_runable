from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
import json
from skipshop.models import skipModel
from skipshop.serializers import skipSerializer

@csrf_exempt
def skipshop_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        shopId = data.get('shopId')
        remark = data.get('remark')

        # Create a dictionary for the input data
        product_data = {
            'shopId': shopId,
            'remark': remark,
        }

        # Serialize the data
        serializer = skipSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database

            response_data = {
                "message": "Success",
                "message_code": "1000_OK",
                "message_data": product_data
            }

            return JsonResponse(response_data, status=status.HTTP_201_CREATED)  # Use 201 status code for successful creation
        else:
            error_data = {
                "message_text": "Failure",
                "message_code": 999,
                "message_data": serializer.errors
            }

            return JsonResponse(error_data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "message_text": "Failure",
            "message_code": 999,
            "message_data": {}
        }

    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
