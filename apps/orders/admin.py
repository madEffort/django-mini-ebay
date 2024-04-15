from django.contrib import admin
from .models import *


class OrderDetailInline(admin.StackedInline):
    model = OrderDetail
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass
