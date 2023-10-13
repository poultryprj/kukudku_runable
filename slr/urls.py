# slr/urls.py
from django.urls import path
from django.urls import re_path as url

from slr import views
urlpatterns = [
    url(r'^routes$', views.route_list),
    path('routes/<int:route_id>/', views.route_detail),


    # Add other URL patterns as needed
]
