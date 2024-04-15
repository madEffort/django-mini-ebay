from django.contrib.auth.models import AbstractUser
from django.db import models


# 기본 유저 모델에 이메일을 추가로 받을 수 있게 확장 + 판매자인지 아닌지 확장
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
