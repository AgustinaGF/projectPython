
from django.shortcuts import render
from products.models import Products

# Create your views here.


def product(request):
    producto = Products.objects.all()
    context = {'producto': producto}
    return render(request, 'card_product.html', context=context)

def create_products(request):
    return render(request, 'create_product.html')