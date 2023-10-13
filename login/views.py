# # #from django.shortcuts import render

# # Create your views here.
# # from django.views import View
# # from django.http import JsonResponse
# # import json
# # from login.models import LoginModel
# # from django.utils.decorators import method_decorator
# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework import status

# # @method_decorator(csrf_exempt, name='dispatch')
# # class LoginViews(View):
# #     def post(self, request):

# #         data = json.loads(request.body.decode("utf-8"))
# #         u_name = data.get('user_mobile_number')
# #         u_pass = data.get('pin')
        
# #         product_data = {
# #             'user_mobile_number': u_name,
# #             'pin': u_pass,
            
# #         }
        
# #         user_id = LoginModel.objects.create(**product_data)

# #         data = {
# #             "loginstatus":[{
# #             "message_text": f"User logged in successfully",
# #             "status_code" : f"1000_OK",
# #             "user" : u_name,
# #         }]
# #         }
# #         return JsonResponse(data, status=200)

# import json

# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from login.models import LoginModel
# from login.serializers import loginSerializer


# @method_decorator(csrf_exempt, name='dispatch')
    
    
# def login_view(request):
    
#     if request.method=='GET':
#         # users = LoginModel.objects.filter()
#         # logins_serializer=loginSerializer(users,many=True)
#         # return JsonResponse(logins_serializer.data,safe=False)
#         users = LoginModel.objects.filter()
#         logins_serializer = loginSerializer(users, many=True)
#         data = logins_serializer.data

#         data1 = {
#                 "message_text": "Success",
#                 "message_code": 1000,
#                 "message_data": data,
#             }

#         return JsonResponse(data1, safe=False)
    
#     elif request.method=='POST':
#         data = json.loads(request.body.decode("utf-8"))
#         u_name = data.get('user_mobile_number')
#         u_pass = data.get('user_pin')
       
#         user_data = LoginModel.objects.filter(user_mobile_number='8830474415',user_pin='abcdef')
#         logins_serializer = loginSerializer(user_data, many=True)
       
#         if not u_name or u_name.strip() == "":
#             return JsonResponse({"error": "User mobile number cannot be blank, zero, or whitespace."} , status=status.HTTP_400_BAD_REQUEST)
        
#         if not u_pass or u_pass.strip() == "":
#             return JsonResponse({"error": "Pin cannot be blank, zero, or whitespace."} , status=status.HTTP_400_BAD_REQUEST)

#         data1 = {
#                 "message_text": "Success",
#                 "message_code": 1000,
#                 "message_data": data,
#             }    

#         return JsonResponse(data1, safe=False)
#     # Perform further validation or processing as needed
    
#     product_data = {
#         'user_mobile_number':8830821972,
#         'user_pin': 12345,
#     }

#         #user_id = LoginModel.objects.create(**product_data)

#     if u_name == "user_mobile_number" and u_pass == "user_pin":
#         data = {
#                 "message_text": "Success",
#                 "message_code": 1000,
#                 "message_data": product_data,
#             }

#         return JsonResponse(data, status=status.HTTP_200_OK)
#     else:   
#         data = {
#                 "message_text": "Failure",
#                 "message_code": 999,
#                 "message_data": {},
#             }
        
#         return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
    
#     #return JsonResponse(data,status=200)



import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from login.models import LoginModel
from login.serializers import loginSerializer

@method_decorator(csrf_exempt, name='dispatch')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        u_name = data.get('user_mobile_number')
        u_pass = data.get('user_pin')
        
        if not u_name or not u_pass:
            return JsonResponse({"error": "User mobile number and pin are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_data = LoginModel.objects.get(user_mobile_number=u_name,user_pin=u_pass)
        except LoginModel.DoesNotExist:
            return JsonResponse({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": {},
            }, status=status.HTTP_404_NOT_FOUND)

        if u_pass != user_data.user_pin:
            return JsonResponse({"error": "Invalid pin."}, status=status.HTTP_401_UNAUTHORIZED)

        data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": {
                "user_mobile_number": user_data.user_mobile_number,
                "user_pin": user_data.user_pin
            },
        }

        return JsonResponse(data, status=status.HTTP_200_OK)

    if request.method == 'GET':
        users = LoginModel.objects.filter()
        logins_serializer = loginSerializer(users, many=True)
        data = logins_serializer.data

        data1 = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": data,
        }

        return JsonResponse(data1, safe=False)


