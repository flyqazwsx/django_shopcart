from django.shortcuts import render, redirect
from shopcart.forms import ProductForm
from .models import Product
# Create your views here.


def create_shop(request):
    form = ProductForm()
    if request.method == 'POST':
        print('POST')
        if request.user.is_authenticated:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('view_shop')
    context = {
        'view_shop': view_shop,
        'form': form
    }

    return render(request, './shopcart/create_shop.html', context)


def view_shop(request):

    shops = Product.objects.all()

    return render(request, './shopcart/view_shop.html', {'shops': shops})
