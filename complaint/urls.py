
    
#urls.py
from django.urls import re_path as url
from complaint import views

urlpatterns = [
    # url(r'^complaint$', views.complaint_view),
    url(r'^complaint$', views.upload_complaint)
 ]