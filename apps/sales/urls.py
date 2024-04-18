from django.urls import path
from . import views

app_name = 'sales'
urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('register/', views.register_product, name='register_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]