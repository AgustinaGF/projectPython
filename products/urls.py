from django.urls import path

from products.views import product

urlpatterns = [

    path('products/', product, name="template")

]
