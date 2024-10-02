from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
def products(request):
    return render(request, 'products.html')
def cart(request):
    return render(request, 'cart.html')