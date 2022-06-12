
from pydoc import describe
from unicodedata import name
from django.shortcuts import render
from products.models import Products
from products.forms import Product_form
from django.http import HttpResponse

# Create your views here.


def product(request):
    producto = Products.objects.all()
    context = {'producto': producto}
    return render(request, 'card_product.html', context=context)

def create_products(request):
    if request.method == "GET":
        form = Product_form()
        context = {'form': form}
        return render(request, 'create_product.html', context=context)
    else:
        form= Product_form(request.POST)
        if form.is_valid():
            new_product= Products.objects.create(
                name = form.cleaned_data["name"],
                type = form.cleaned_data["type"],
                price = form.cleaned_data["price"],
                description = form.cleaned_data["description"],
                in_stock = form.cleaned_data["in_stock"],
            )
            context={"new_product":new_product}
        return HttpResponse (request, 'create_product.html', context=context)