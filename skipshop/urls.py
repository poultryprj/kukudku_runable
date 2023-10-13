from django.urls import path
from skipshop import views
from django.urls import re_path as url


urlpatterns = [
    url(r'^skipshop$',views.skipshop_view),
]
