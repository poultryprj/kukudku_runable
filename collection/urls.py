from django.urls import re_path as url
from collection import views

urlpatterns = [
    url(r'^collection$', views.collection_view),
    url(r'^collectioninfo$', views.collectioninfo_view),
    url(r'^collectionskip$', views.collectionskip_view),
]