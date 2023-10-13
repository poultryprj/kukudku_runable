# # import json
# # from django.http import JsonResponse
# # from django.utils.decorators import method_decorator
# # from django.views.decorators.csrf import csrf_exempt
# # from collection.models import collectionModel
# # from collection.serializers import collectionSerializer
# # from rest_framework import status

# # # Define the payment options array
# # ALLOWED_PAYMENT_OPTIONS = [
# #     'Credit card',
# #     'Debit card',
# #     'Cheque',
# #     'UPI',
# #     'Cash',
# # ]

# # paid_amount = [
    
# # ]


# # @method_decorator(csrf_exempt, name='dispatch')
# # def collection_view(request):
# #     if request.method == 'POST':
# #         data = json.loads(request.body.decode("utf-8"))
# #         shopId = data.get('shopid')
# #         lati = data.get('lati')
# #         longi = data.get('longi')
# #         paymentmethod = data.get('paymentmethod')
# #         paidamount = data.get('paidamount')

        
        
# #         for method in paymentmethod:
# #             if method not in ALLOWED_PAYMENT_OPTIONS:
# #                 return JsonResponse(
# #                     {
# #                         "message_text": f"Invalid payment method: {method}",
# #                         "message_code": 999,
# #                         "message_data": {},
# #                     },
# #                     status=status.HTTP_400_BAD_REQUEST
# #                 )

# #         # You can continue with the rest of your code here, like saving the data to the database
# #         # For example:
# #         collection_info = collectionModel.objects.filter()
# #         collection_serializer = collectionSerializer(collection_info, many=True)

# #         product_data = {
# #             'shopid': shopId,
# #             'lati': lati,
# #             'longi': longi,
# #             'paymentmethod': paymentmethod,
# #             'paidamount': paidamount, 
# #         }

# #         data = {
# #             "message_text": "Success",
# #             "message_code": 1000,
# #             "message_data": product_data,
# #         }

# #         return JsonResponse(data, status=status.HTTP_200_OK)

# #     data = {
# #         "message_text": "Failure",
# #         "message_code": 999,
# #         "message_data": {},
# #     }

# #     return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)



# import json
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from collection.models import collectionModel , collectionInfo, collectionSkipped
# from collection.serializers import collectionSerializer
# from rest_framework import status

# # Define the payment options array
# ALLOWED_PAYMENT_OPTIONS = [
#     'Cash',
#     'Cheque',
#     'NEFT/IMPS',
#     'GPAY',
#     'PAYTM',
#     'PHONEPE'
# ]

# # Initialize a dictionary to store paid amounts for each payment method
# paid_amount_by_method = {method: 0 for method in ALLOWED_PAYMENT_OPTIONS}
# @method_decorator(csrf_exempt, name='dispatch')
# def collection_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode("utf-8"))
#         shopId = data.get('shopId')
#         lati = data.get('lati')
#         longi = data.get('longi')
#         paymentmethod = data.get('paymentmethod')
#         paidamount = data.get('paidamount')

#         # Validate payment methods
#         invalid_payment_methods = [method for method in paymentmethod if method not in ALLOWED_PAYMENT_OPTIONS]
#         if invalid_payment_methods:
#             return JsonResponse(
#                 {
#                     "message_text": f"Invalid payment methods: {', '.join(invalid_payment_methods)}",
#                     "message_code": 999,
#                     "message_data": {},
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # Create and save collection model instance
#         collection_instance = collectionModel.objects.create(
#             shopId=shopId,
#             lati=lati,
#             longi=longi,
#             paymentmethod=paymentmethod,
#             paidamount=paidamount
#         )
        
#         # # Save payment methods and amounts
#         # for method, amount in zip(paymentmethod, paidamount):
#         #     collection_instance.paymentmethod.add(method)
#         #     paid_amount_instance = collectionInfo.objects.create(
#         #         collection=collection_instance,
#         #         paymentmethod=method,
#         #         paidamount=amount,
#         #     )
#         #     paid_amount_instance.save()

#         data = {
#             "message_text": "Success",
#             "message_code": 1000,
#             "message_data": {
#                 'shopId': shopId,
#                 'lati': lati,
#                 'longi': longi,
#                 'paymentmethod': paymentmethod,
#                 'paidamount': paidamount,
#             },
#         }

#         return JsonResponse(data, status=status.HTTP_200_OK)

#     data = {
#         "message_text": "Failure",
#         "message_code": 999,
#         "message_data": {},
#     }

#     return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(csrf_exempt, name='dispatch')
# def collectioninfo_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode("utf-8"))
#         collectionId = data.get('collectionid') 
#         collectionDate = data.get('collectiondate')
#         collectionTime = data.get('collectiontime')
#         userId = data.get('userid')
#         shopId = data.get('shopid')
#         collectionMode = data.get('collectionmode')
#         collectionAmount = data.get('collectionamount')
#         collectionVerified = data.get('collectionverified')
#         collectionConfimed = data.get('collectionconfirmed')
#         accountCredited = data.get('accountcredited')
        
#         collection_data = {
#             'collectionid' : collectionId,
#             'userid' : userId,
#             'shopid' : shopId,
#             'collectionmode' : collectionMode, 
#             'collectionamount' : collectionAmount,
#             'collectionverified' : collectionVerified,
#             'collectionconfirmed' : collectionConfimed,
#             'accountcredited' : accountCredited
#         }
        
        
#         data = {
#             "message_text": "Success",
#             "message_code": 1000,
#             "message_data": collection_data,
#         }
        
#         return JsonResponse(data, status=status.HTTP_200_OK)
#     else:
#         data = {
#         "message_text": "Failure",
#         "message_code": 999,
#         "message_data": {},
#     }

#     return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_exempt, name='dispatch')
# def collectionskip_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode("utf-8"))
#         collectionId = data.get('collectionid')
#         userId = data.get('userid')
#         shopId = data.get('shopid')
#         remark = data.get('remark')
#         confirmed = data.get('confirmed')
        
#         collection_data = {
#             'collectionid' : collectionId,
#             'userid' : userId,
#             'shopid' : shopId,
#             'remark' : remark,
#             'confirmed' : confirmed
#         }
        
        
#         data = {
#             "message_text": "Success",
#             "message_code": 1000,
#             "message_data": collection_data,
#         }
        
#         return JsonResponse(data, status=status.HTTP_200_OK)
#     else:
#         data = {
#         "message_text": "Failure",
#         "message_code": 999,
#         "message_data": {},
#     }

#     return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
















from django.shortcuts import render
import json
import boto3
from botocore.exceptions import NoCredentialsError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from collection.models import collectionModel
from rest_framework import status
import time
# Define the payment options array
import json
import boto3
from botocore.exceptions import NoCredentialsError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collection.models import collectionModel
from rest_framework import status
from django.db.models import Sum

# Define the payment options array
ALLOWED_PAYMENT_OPTIONS = [
    'Cash',
    'Cheque',
    'NEFT/IMPS',
    'GPAY',
    'PAYTM',
    'PHONEPE'
]

# Set your AWS S3 credentials and bucket name.
AWS_ACCESS_KEY_ID = 'AKIA6AL6FGIVCDBX5BHU'
AWS_SECRET_ACCESS_KEY = 'SmnW00RAV2g6JAqfNMTuNPYZZkJr6hslgIVryjnc'
S3_BUCKET_NAME = 'kukudku'
S3_PREFIX = 'collection/'  # Object key prefix within the bucket

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
@method_decorator(csrf_exempt, name='dispatch')
def collection_view(request):
    if request.method == 'POST':
        shopId = request.POST.get('shopId')
        lati = request.POST.get('lati')
        longi = request.POST.get('longi')
        paymentmethods = request.POST.getlist('paymentmethod')  # Use getlist to get multiple values
        paidamount = request.POST.get('paidamount')
        cheque_photo = request.FILES.get('cheque_photo')
        gpay_photo = request.FILES.get('gpay_photo')
        phonepe_photo = request.FILES.get('phonepe_photo')
        paytm_photo = request.FILES.get('paytm_photo')
        neft_imps_photo = request.FILES.get('neft_imps_photo')



        # invalid_payment_methods = [method for method in paymentmethods if method not in ALLOWED_PAYMENT_OPTIONS]
        # if invalid_payment_methods:
        #     return JsonResponse(
        #         {
        #             "message_text": f"Invalid payment methods: {', '.join(invalid_payment_methods)}",
        #             "message_code": 999,
        #             "message_data": {},
        #         },
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

        try:
            # Define S3 object keys for each payment method photo
            timestamp = int(time.time())
            cheque_key = None
            gpay_key = None
            phonepe_key = None
            paytm_key = None
            neft_imps_key = None

            # Upload cheque photo if it exists
            if cheque_photo:
                cheque_key = f'{S3_PREFIX}cheques/{shopId}_{timestamp}_{cheque_photo.name}'
                s3_client.upload_fileobj(
                    cheque_photo,
                    S3_BUCKET_NAME,
                    cheque_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

            # Upload other photos if they exist
            if gpay_photo:
                gpay_key = f'{S3_PREFIX}gpay/{shopId}_{timestamp}_{gpay_photo.name}'
                s3_client.upload_fileobj(
                    gpay_photo,
                    S3_BUCKET_NAME,
                    gpay_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

            if phonepe_photo:
                phonepe_key = f'{S3_PREFIX}phonepe/{shopId}_{timestamp}_{phonepe_photo.name}'
                s3_client.upload_fileobj(
                    phonepe_photo,
                    S3_BUCKET_NAME,
                    phonepe_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

            if paytm_photo:
                paytm_key = f'{S3_PREFIX}paytm/{shopId}_{timestamp}_{paytm_photo.name}'
                s3_client.upload_fileobj(
                    paytm_photo,
                    S3_BUCKET_NAME,
                    paytm_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

            if neft_imps_photo:
                neft_imps_key = f'{S3_PREFIX}neft_imps/{shopId}_{timestamp}_{neft_imps_photo.name}'
                s3_client.upload_fileobj(
                    neft_imps_photo,
                    S3_BUCKET_NAME,
                    neft_imps_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

            # Create and save collection model instance
            collection_instance = collectionModel.objects.create(
                shopId=shopId,
                lati=lati,
                longi=longi,
                paymentmethod=paymentmethods,  # Use paymentmethods, which is a list
                paidamount=paidamount,
                cheque_photo=f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{cheque_key}' if cheque_key else None,
                gpay_photo=f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{gpay_key}' if gpay_key else None,
                phonepe_photo=f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{phonepe_key}' if phonepe_key else None,
                paytm_photo=f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{paytm_key}' if paytm_key else None,
                neft_imps_photo=f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{neft_imps_key}' if neft_imps_key else None,
            )

            data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": {
                    'shopId': shopId,
                    'lati': lati,
                    'longi': longi,
                    'paymentmethod': paymentmethods,
                    'paidamount': paidamount,
                },
            }

            return JsonResponse(data, status=status.HTTP_200_OK)

        except NoCredentialsError:
            return JsonResponse({'error': 'AWS credentials not found or invalid'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = {
        "message_text": "Failure",
        "message_code": 999,
        "message_data": {}
    }
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)





@method_decorator(csrf_exempt, name='dispatch')
def collectioninfo_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        collectionId = data.get('collectionid') 
        collectionDate = data.get('collectiondate')
        collectionTime = data.get('collectiontime')
        userId = data.get('userid')
        shopId = data.get('shopid')
        collectionMode = data.get('collectionmode')
        collectionAmount = data.get('collectionamount')
        collectionVerified = data.get('collectionverified')
        collectionConfimed = data.get('collectionconfirmed')
        accountCredited = data.get('accountcredited')
        
        collection_data = {
            'collectionid' : collectionId,
            'userid' : userId,
            'shopid' : shopId,
            'collectionmode' : collectionMode, 
            'collectionamount' : collectionAmount,
            'collectionverified' : collectionVerified,
            'collectionconfirmed' : collectionConfimed,
            'accountcredited' : accountCredited
        }
        
        
        data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": collection_data,
        }
        
        return JsonResponse(data, status=status.HTTP_200_OK)
    else:
        data = {
        "message_text": "Failure",
        "message_code": 999,
        "message_data": {},
    }

    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
def collectionskip_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        collectionId = data.get('collectionid')
        userId = data.get('userid')
        shopId = data.get('shopid')
        remark = data.get('remark')
        confirmed = data.get('confirmed')
        
        collection_data = {
            'collectionid' : collectionId,
            'userid' : userId,
            'shopid' : shopId,
            'remark' : remark,
            'confirmed' : confirmed
        }
        
        
        data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": collection_data,
        }
        
        return JsonResponse(data, status=status.HTTP_200_OK)
    else:
        data = {
        "message_text": "Failure",
        "message_code": 999,
        "message_data": {},
    }

    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
