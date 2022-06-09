from django.urls import path

from products.views import product

urlpatterns = [

    path('create-products/', product, name="template")

]
