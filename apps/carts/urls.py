from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('update/', views.update_cart, name='update_cart'),
]