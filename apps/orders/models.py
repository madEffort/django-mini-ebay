from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product, ProductSnapshot

User = get_user_model()


# 주문 모델
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    STATUS_CHOICES = [
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="processing"
    )
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# 주문 상세 모델
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_snapshot = models.ForeignKey(ProductSnapshot, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f"Detail for Order {self.order.id}"
