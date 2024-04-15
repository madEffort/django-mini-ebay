from django.contrib import admin
from .models import Cart, CartDetail

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartDetail)
class CartDetailAdmin(admin.ModelAdmin):
    pass
