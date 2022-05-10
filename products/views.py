from django.shortcuts import render


def index(request):
    context = {'title': 'MyShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'MyShop - Products'}
    return render(request, 'products/products.html', context)
