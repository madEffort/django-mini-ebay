from django.urls import path
from apps.products.models import Product
from . import views

app_name = 'sales'
urlpatterns = [
    path('', views.register_product, name='register_product'),
]