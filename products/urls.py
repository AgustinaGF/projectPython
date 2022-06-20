from unicodedata import name
from django.urls import path

from products.views import product,create_products,search_product_view,genre,artists,detail_products,delete_product

urlpatterns = [
    path('artist/',artists, name="artist"),
     path('genre/', genre, name="genre"),
    path('products/', product, name="template"),
    path('detail-products/<int:pk>/', detail_products, name="detail_products"),
    path('create-products/', create_products, name="create-products"),
    path('search-product/', search_product_view, name="search_product_view"),
    path('delete-product/<int:pk>/', delete_product, name="delete_product"),
]
