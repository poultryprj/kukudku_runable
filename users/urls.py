from users import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^users$',views.user_view),
    url(r'^usersrole/$',views.userrole_view),
    url(r'^roles/$',views.role_view),
    url(r'^roles/(?P<role_id>\d+)/$', views.role_view)
]