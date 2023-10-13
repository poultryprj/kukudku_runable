from django.urls import re_path as url
from login import views

# urlpatterns = [
#     path('login/',LoginViews.as_view()),
# ]

urlpatterns = [
    url(r'^login$',views.login_view),
]

# from django.urls import path
# #from login.views import login_view

# urlpatterns = [
#     path('login/', login_view, name='login'),
#     # Other URL patterns
# ]
