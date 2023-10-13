from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from users.models import userModel , userRoles, Roles

def user_view(request):
    if request.method == 'GET':
        usersinfo = userModel.objects.filter()
        
    user = []    
    for user_info in usersinfo:
        user.append({
        'username': user_info.userName,
        'usermobileno': user_info.userMobileNo,
        'useralternateno': user_info.userAlternateNo,
        'userpassword': user_info.userPassword,
        'userlevel': user_info.userLevel,
        })

    
    data = {
        'message_text': 'Success',
        'message_code': 1000,
        'message_data': user
    }
    
    return JsonResponse(data , status=status.HTTP_200_OK)

def userrole_view(request):
    if request.method == 'GET':
        roleinfo = userRoles.objects.filter()
        
    user_role = []    
    for role_info in roleinfo:
        user_role.append({
        'userrole':role_info.userRoleId,
        'userid':role_info.userId,
        'roleid':role_info.roleId,
        'roleactive':role_info.roleActiveYN
        })

    
    data = {
        'message_text': 'Success',
        'message_code': 1000,
        'message_data': user_role
    }
    
    return JsonResponse(data , status=status.HTTP_200_OK)


from django.http import JsonResponse
from users.models import Roles  # Replace 'yourapp' with the actual name of your Django app

def role_view(request, role_id=None):
    if request.method == 'GET':
        if role_id is None:
            # No role_id provided, list all roles
            roles = Roles.objects.all()

            # Create a list of role data from the query results
            role_data = []
            for role in roles:
                role_data.append({
                    'roleid': role.roleId,
                    'rolename': role.roleName,
                })

            # Create the response JSON data
            data = {
                'message_text': 'Success',
                'message_code': 1000,
                'message_data': role_data
            }

            return JsonResponse(data, status=status.HTTP_200_OK)  # Use status=200 for HTTP 200 OK response
        else:
            # Retrieve a specific role by role_id
            try:
                role = Roles.objects.get(roleId=role_id)
                
                # Create a dictionary with role data
                role_data = {
                    'roleid': role.roleId,
                    'rolename': role.roleName,
                }

                # Create the response JSON data
                data = {
                    'message_text': 'Success',
                    'message_code': 1000,
                    'message_data': role_data
                }

                return JsonResponse(data, status=status.HTTP_200_OK)  # Use status=200 for HTTP 200 OK response
            except Roles.DoesNotExist:
                return JsonResponse(message="Role does not exist", status=status.HTTP_404_NOT_FOUND)


    
