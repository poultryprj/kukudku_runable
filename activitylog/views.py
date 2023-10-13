from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import ArrayObject

@csrf_exempt
def activitylog_view(request, object_id=None):
    if request.method == 'POST':
        user = User.objects.first()  # Replace with proper user authentication
        data = request.POST.get('data')
        obj = ArrayObject.objects.create(created_by=user, last_modified_by=user)
        return JsonResponse({"message": "Object created successfully."})
    
    if request.method == 'GET':
        objects = ArrayObject.objects.filter(is_deleted=False)
        data = [{
                 "created_on": obj.created_on,
                 "created_by": obj.created_by.username if obj.created_by else None,
                 "last_modified_on": obj.last_modified_on,
                 "last_modified_by": obj.last_modified_by.username if obj.last_modified_by else None,
                 "is_deleted": obj.is_deleted,
                 "deleted_by": obj.deleted_by.username if obj.deleted_by else None
                 } for obj in objects]
        return JsonResponse(data, safe=False)
    
    if request.method == 'DELETE' and object_id is not None:
        try:
            user = User.objects.first()  # Replace with proper user authentication
            obj = ArrayObject.objects.get(pk=object_id)
            obj.soft_delete(user) 
            return JsonResponse({"message": "Object soft deleted."})
        except ArrayObject.DoesNotExist:
            return JsonResponse({"message": "Object not found."}, status=404)
