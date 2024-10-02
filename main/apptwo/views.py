from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def product(request):
    return render(request, 'products.html')
def carts(request):
    return render(request, 'cart.html')