from django.shortcuts import render
from django.urls import reverse
from products.models import Products,Musical_genre,Artist
from products.forms import Product_form
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
# Create your views here.

class List_product(ListView):
    model= Products
    template_name='card_product.html'
    queryset = Products.objects.filter(in_stock=True)

class Detail_product(DetailView):
    model = Products
    template_name= 'product_detail.html'

class Create_products(LoginRequiredMixin,CreateView):
    model = Products
    template_name = 'create_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_products', kwargs={'pk':self.object.pk})

class Delete_products(DeleteView):
    model = Products
    template_name = 'delete_product.html'

    def get_success_url(self):
        return reverse('list_products')

class Update_product(UpdateView):
    model = Products
    template_name = 'update_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_products', kwargs={'pk':self.object.pk})
    

def artists(request):
    artist = Artist.objects.all()
    context = {'artist': artist}
    return render(request, 'artists.html', context=context)

def genre (request):
    genre = Musical_genre.objects.all()
    context ={'genre': genre}
    return render(request, 'genre.html', context=context)

def search_product_view(request):
    print(request.GET)
    products = Products.objects.filter(name__icontains=request.GET['Search'])
    context= {'products':products}
    return render (request, 'search_product.html', context=context)

def about_me(request):
    return render (request,'about_me.html')

