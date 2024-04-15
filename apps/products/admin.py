from django.contrib import admin
from .models import Category, Product


class ProductInline(admin.StackedInline):
    model = Product
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
