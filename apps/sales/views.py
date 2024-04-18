from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from apps.products.forms import ProductForm
from apps.products.models import Product
from apps.orders.models import OrderDetail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# 상품 등록
@login_required
def register_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                seller=request.user,
                name=form.cleaned_data.get("name"),
                description=form.cleaned_data.get("description"),
                image=form.cleaned_data.get("image"),
                price=form.cleaned_data.get("price"),
                stock_quantity=form.cleaned_data.get("stock_quantity"),
                category=form.cleaned_data.get("category"),
            )
            return redirect("home")
    else:
        form = ProductForm()

    return render(request, "sales/register_product.html", {"form": form})

@login_required
def edit_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = ProductForm(instance=product)

    context = {"form": form, "product": product}
    return render(request, "sales/edit_product.html", context)

# 상품 삭제
@login_required
def delete_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("home")

    return HttpResponse("Failed to delete product")

@login_required
def sales_list(request):
    # 현재 로그인한 사용자가 판매자인 경우 해당 판매자가 등록한 상품 중 주문된 상품들을 조회합니다.
    # 사용자 모델에 따라 판매자를 어떻게 식별할 수 있는지에 따라 코드가 달라질 수 있습니다.
    # 예를 들어, 판매자 사용자 그룹을 사용한다면 그룹을 기반으로 필터링할 수 있습니다.
    
    # 판매자가 등록한 상품들의 ID 목록을 가져옵니다.
    seller_products_ids = request.user.product_set.values_list('id', flat=True)

    # 주문 상세(OrderDetail) 중에 해당 상품들이 포함된 것들을 가져옵니다.
    sales_list = OrderDetail.objects.filter(product_snapshot__product__id__in=seller_products_ids)
    # 조회된 주문 상세 정보를 템플릿으로 전달합니다.

    return render(request, 'sales/sales_list.html', {'sales_list': sales_list})
