from django.urls import path
from .import views

urlpatterns = [
    path('camera/', views.Camera, name='camera'),
    path('map/', views.Map, name='map'),
    
]