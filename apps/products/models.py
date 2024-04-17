from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# 상품 모델
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:  # 상품이 이미 데이터베이스에 존재하는 경우 (즉, 이것이 '업데이트' 작업임)
            orig = Product.objects.get(pk=self.pk)
            if (orig.name != self.name or orig.price != self.price):  # 이름이나 가격에 변화가 있는 경우
                self.create_snapshot()
            if orig.image != self.image:  # 이미지 변경 후 이전 이미지 삭제
                orig.image.delete(save=False)
        super().save(*args, **kwargs)
    
    def create_snapshot(self):
        ProductSnapshot.objects.create(
            product=self,
            seller=self.seller,
            name=self.name,
            description=self.description,
            price=self.price,
            stock_quantity=self.stock_quantity,
            category=self.category
        )

# 상품 스냅샷 모델 (판매자가 상품 수정을 할 경우 구매내역의 상품 정보(가격)은 바뀌면 안되기 때문)
class ProductSnapshot(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    snapshot_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-snapshot_date']
    
    def __str__(self):
        return f"Snapshot of {self.name} on {self.snapshot_date.strftime('%Y-%m-%d')}"