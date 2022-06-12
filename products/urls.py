from unicodedata import name
from django.urls import path

from products.views import product,create_products,search_product_view

urlpatterns = [

    path('products/', product, name="template"),
    path('create-products/', create_products, name="create-products"),
    path('search-product/',search_product_view, name="search_product_view")
]
