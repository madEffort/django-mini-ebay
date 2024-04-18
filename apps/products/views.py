from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product, Category
from apps.carts.models import Cart, CartDetail
from apps.carts.forms import AddToCartForm
from apps.orders.models import Order
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductList(ListView):
    model = Product
    template_name = "products/product_list.html"
    paginate_by = 12
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["orders"] = Order.objects.filter(user=self.request.user)
            context['products'] = Product.objects.filter(seller=self.request.user)
            cart, _ = Cart.objects.get_or_create(user=self.request.user)
            context['cart'] = cart
            context['categories'] = Category.objects.all()
        else:
            context["orders"] = None
            context['products'] = None
            context['cart'] = None
            context['categories'] = Category.objects.all()
        return context


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        # 사용자가 로그인이 되어있을 경우에만 아래의 코드 실행
        if request.user.is_authenticated:
            # 폼에서 상품의 재고 수 이상을 입력 받으면 유효성 검사를 통과하지 못하게 초기값 설정
            form = AddToCartForm(request.POST, max_value=product.stock_quantity)

            # 장바구니에 담기 버튼을 눌렀을 경우
            if "add_to_cart" in request.POST:
                if form.is_valid():
                    quantity = int(form.cleaned_data.get("quantity"))
                    if quantity <= product.stock_quantity:
                        # 카트 생성 혹은 이미 있을경우 가져오기
                        cart, created = Cart.objects.get_or_create(user=request.user)
                        cart_detail, created = CartDetail.objects.get_or_create(
                            cart=cart, product=product
                        )

                        if not created:
                            cart_detail.quantity += quantity
                        else:
                            cart_detail.quantity = quantity
                        cart_detail.save()
                        return redirect("carts:cart")
                else:
                    context = {"object": product, "form": form}
                    return render(request, "products/product_detail.html", context)

            # 바로 주문하기 버튼을 눌렀을 경우
            if "order_now" in request.POST:
                if form.is_valid():
                    quantity = int(form.cleaned_data.get("quantity"))
                    if quantity <= product.stock_quantity:
                        cart, created = Cart.objects.get_or_create(user=request.user)
                        cart_detail, created = CartDetail.objects.get_or_create(
                            cart=cart, product=product
                        )

                        if not created:
                            cart_detail.quantity += quantity
                        else:
                            cart_detail.quantity = quantity
                            
                        product.stock_quantity -= quantity
                        product.save()

                        cart_detail.save()
                    return redirect("orders:order_create")
                # 유효성 검사를 통과하지 못했을 경우 에러메시지를 form에 넣어줌
                else:
                    context = {"object": product, "form": form}
                    return render(request, "products/product_detail.html", context)
        # 사용자가 로그인이 되어있지 않을 경우 로그인 페이지로 이동
        else:
            return redirect("accounts:login")
    # GET으로 넘어왔을 경우 Form 생성
    else:
        form = AddToCartForm(max_value=product.stock_quantity)

    context = {"object": product, "form": form}

    return render(request, "products/product_detail.html", context)

def product_category(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        category_id = data['categoryId']
        if data['mode'] == 0:
            products = Product.objects.filter(seller=request.user, category_id=category_id)
        else:
            products = Product.objects.filter(category_id=category_id)
        context = {
            'category_products': serialize('json', products)
        }
        return JsonResponse(context)