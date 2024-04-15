from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart

# 데코레이터를 사용하여 로그인 안되어 있을 경우 로그인 페이지로
@login_required
def cart(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = cart.cartdetail_set.all()
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }

    return render(request, "carts/cart.html", context)
