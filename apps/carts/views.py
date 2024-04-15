from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cart, CartDetail
from django.http import JsonResponse

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

# 카트에서 동적으로 상품 빼거나 추가하기
@login_required
@require_POST
@csrf_exempt
def update_cart(request):
    data = json.loads(request.body)
    cart_item_id = data.get('cartItemId')
    quantity = data.get('quantity')
    remove = data.get('remove', False)

    cart_item = CartDetail.objects.get(id=cart_item_id)
    if remove:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    total_amount = calculate_total(request.user)
    return JsonResponse({'total_amount': total_amount})

def calculate_total(user):
    cart = Cart.objects.get(user=user)
    total = sum(item.product.price * item.quantity for item in cart.cartdetail_set.all())
    return total