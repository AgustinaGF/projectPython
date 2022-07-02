from django.urls import path

from products.views import List_product,Detail_product,Create_products,Delete_products,Update_product,search_product_view,genre,artists

urlpatterns = [
    path('artist/',artists, name="artist"),
    path('genre/', genre, name="genre"),
    path('products/', List_product.as_view(), name="list_products"),
    path('detail-products/<int:pk>/', Detail_product.as_view(), name="detail_products"),
    path('create-products/', Create_products.as_view(), name="create-products"),
    path('search-product/', search_product_view, name="search_product_view"),
    path('delete-product/<int:pk>/', Delete_products.as_view(), name="delete_product"),
    path('update-product/<int:pk>/', Update_product.as_view(), name="update_product"),
]
