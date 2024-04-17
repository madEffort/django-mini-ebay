from django.shortcuts import render, redirect, get_object_or_404
from apps.products.forms import ProductForm
from apps.products.models import Product
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
