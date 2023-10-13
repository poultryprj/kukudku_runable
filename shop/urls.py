
from shop import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^shop$',views.shop_view),
    url(r'^shopowner$',views.shopowner_view),
    url(r'^shoproute$',views.shoproute_view),
    url(r'^shopbalance$',views.shopbalance_view)
]