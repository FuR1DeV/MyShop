import os
import json

from django.shortcuts import render

module_dir = os.path.dirname(__file__)


def index(request):
    context = {'title': 'MyShop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    prod = json.load(open(file_path, encoding='utf-8'))
    context = {'title': 'MyShop - Products',
               'products': prod}
    return render(request, 'products/products.html', context)
