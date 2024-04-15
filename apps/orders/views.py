from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from apps.carts.models import Cart
from apps.products.models import ProductSnapshot
from .models import Order, OrderDetail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def order_create(request):
    user = request.user
    cart = Cart.objects.get(user=user)

    # 역참조를 통해 카트에 담긴 것들을 가져옴
    cart_items = cart.cartdetail_set.all()

    # 총 얼마인지 카트에 담긴 상품을 반복문 돌려 가격의 총합을 구함
    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":

        # 주문하기 버튼을 누르면 새로운 주문을 생성
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
        )
        
        # 주문에 카트에 담긴 상품들 추가 하여 db에 저장
        for item in cart_items:
            
            snapshot, created = ProductSnapshot.objects.get_or_create(
                product=item.product,
                seller=item.product.seller,
                name=item.product.name,
                description=item.product.description,
                price=item.product.price,
                stock_quantity=item.product.stock_quantity,
                category=item.product.category,
                defaults={'product': item.product}
            )
            
            OrderDetail.objects.create(
                order=order,
                product_snapshot=snapshot,
                quantity=item.quantity,
                price=snapshot.price,
            )

        # DB에 저장한 후에는 카트 비우기
        cart_items.delete()

        messages.success(request, "결제가 완료되었습니다.")
        return redirect("home")

    context = {"cart_items": cart_items, "total_amount": total_amount}

    return render(request, "orders/order.html", context)


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"

    # 본인의 주문내역만 가져오게 쿼리셋 수정
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderLogDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
