from django.shortcuts import render


def login(request):
    context = {'title': 'MyShop - Authorization'}
    return render(request, 'authapp/login.html', context)
