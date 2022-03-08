from django.contrib import admin

from django_bootmin.base import AdminPrintViewMixin, ModelAdminMixin

from .models import Product


@admin.register(Product)
class ProductAdmin(ModelAdminMixin, AdminPrintViewMixin):
    list_display = ["name", "price"]
