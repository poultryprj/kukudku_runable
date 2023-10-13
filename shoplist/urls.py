
from shoplist import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^shoplist$',views.shoplist_view),
]