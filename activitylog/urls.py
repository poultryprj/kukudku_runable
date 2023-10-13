from django.urls import re_path as url
from activitylog import views



urlpatterns = [
    url(r'^activitylog$', views.activitylog_view),
    #url(r'^activitylog/(?P<object_id>\d+)/$', views.activitylog_view),
]

    
