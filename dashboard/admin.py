from django.contrib import admin

# Register your models here.

from dashboard.models import dashboardModel


admin.site.register(dashboardModel)