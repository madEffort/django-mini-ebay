from django.shortcuts import render, redirect
from apps.products.forms import ProductForm
from apps.products.models import Product
# Create your views here.
def register_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                seller=request.user,
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                stock_quantity=form.cleaned_data.get('stock_quantity'),
                category=form.cleaned_data.get('category'),
            )
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'sales/register_product.html', {'form': form})