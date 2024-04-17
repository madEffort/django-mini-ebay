from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductList.as_view(), name="home"),
    path("products/", views.ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/category/", views.product_category, name="product_category"),
]
