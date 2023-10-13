from django.urls import re_path as url
from finalizecollection import views

urlpatterns = [
    url(r'^finalizecollection$', views.finalize_view),
]