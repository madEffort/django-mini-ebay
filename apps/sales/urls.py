from django.urls import path
from apps.products.models import Product
from . import views

app_name = 'sales'
urlpatterns = [
    path('register/', views.register_product, name='register_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]