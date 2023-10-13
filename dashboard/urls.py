from django.urls import re_path as url
from dashboard import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard_view),
]