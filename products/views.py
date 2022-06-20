
from genericpath import exists
from multiprocessing import context
from pydoc import describe
from unicodedata import name
from django.shortcuts import render
from products.models import Products,Musical_genre,Artist
from products.forms import Product_form
from django.http import HttpResponse

# Create your views here.

def artists(request):
    artist = Artist.objects.all()
    context = {'artist': artist}
    return render(request, 'artists.html', context=context)

def genre (request):
    genre = Musical_genre.objects.all()
    context ={'genre': genre}
    return render(request, 'genre.html', context=context)

def product(request):
    product = Products.objects.all()
    context = {'product': product}
    return render(request, 'card_product.html', context=context)

def detail_products(request, pk):
    try:
        prod = Products.objects.get(id=pk)
        context = {'prod':prod}
        return render(request, 'product_detail.html', context=context)
    except:
        context = {'error': 'The product does not exist'}
        return render(request, 'card_product.html', context=context)

def delete_product(request, pk):
    try:
        if request.method == 'GET':
            product_delete = Products.objects.get(id=pk)
            context = {'productDelete':product_delete}
        else:
            product_delete= Products.objects.get(id=pk)
            product_delete.delete()
            context ={'message':'The product was successfully removed'}
        return render(request, 'delete_product.html', context=context )
    except:
        context = {'error': 'The product does not exist'}
        return render(request, 'delete_product.html', context=context)

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
                SKU = form.cleaned_data['SKU'],
                in_stock = form.cleaned_data["in_stock"],
            )
            context={"new_product":new_product}
        return render (request, 'create_product.html', context=context)

def search_product_view(request):
    print(request.GET)
    products = Products.objects.filter(name__icontains=request.GET['Search'])
    context= {'products':products}
    return render (request, 'search_product.html', context=context)