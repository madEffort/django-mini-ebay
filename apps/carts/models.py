from django.db import models
from django.contrib.auth import get_user_model
from apps.orders.models import Product

User = get_user_model()

# 장바구니 모델
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

# 장바구니 상세 모델
class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart {self.cart.id} Detail"