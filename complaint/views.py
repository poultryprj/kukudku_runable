import boto3
from botocore.exceptions import NoCredentialsError
from django.http import JsonResponse
from .models import complaintModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_complaint(request):
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        textfield = request.POST.get('textfield')
        file_upload = request.FILES.get('file_upload')

        if shopname and textfield and file_upload:
            # Set your AWS S3 credentials and bucket name.
            aws_access_key_id = 'AKIA6AL6FGIVCDBX5BHU'
            aws_secret_access_key = 'SmnW00RAV2g6JAqfNMTuNPYZZkJr6hslgIVryjnc'
            s3_bucket_name = 'kukudku'  # Your S3 bucket name
            s3_prefix = 'complaints/'  # Object key prefix within the bucket

            try:
                # Initialize the S3 client.
                s3_client = boto3.client(
                    's3',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                )

                # Define the S3 object key using the original file name.
                s3_object_key = s3_prefix + file_upload.name

                # Upload the file to S3.
                s3_client.upload_fileobj(
                    file_upload,
                    s3_bucket_name,
                    s3_object_key,
                    ExtraArgs={'ACL': 'public-read'},
                )

                # Create a new complaintModel instance.
                complaint = complaintModel(
                    shopname=shopname,
                    textfield=textfield,
                    file_upload=f's3://kukudku/complaints/'
                )
                complaint.save()

                return JsonResponse({'message': 'Complaint and file uploaded successfully'})

            except NoCredentialsError:
                return JsonResponse({'error': 'AWS credentials not found or invalid'})

            except Exception as e:
                return JsonResponse({'error': str(e)})

        else:
            return JsonResponse({'error': 'Missing data or file'})

    return JsonResponse({'error': 'Invalid request method'})



