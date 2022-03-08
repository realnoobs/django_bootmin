from django.contrib import admin
from django.urls import path

from django_bootmin.sites import AdminSite

admin.site.__class__ = AdminSite

urlpatterns = [
    path("admin/", admin.site.urls),
]
