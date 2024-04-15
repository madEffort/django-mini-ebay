from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    # 주문하기을 버튼을 누르면 이동하는 url
    path("logs/", views.OrderList.as_view(), name="order_list"),
    path("logs/<int:pk>/", views.OrderLogDetail.as_view(), name="order_detail"),
    path("create/", views.order_create, name="order_create"),
]
