from django.urls import path
from route import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^route$',views.route_view),
]