from django.urls import path

from products.views import product,create_products

urlpatterns = [

    path('products/', product, name="template"),
    path('create-products/', create_products, name="create-products")
]
