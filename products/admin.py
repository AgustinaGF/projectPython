from django.contrib import admin
from products.models import Products,Musical_genre,Artist

# Register your models here.
admin.site.register(Products)
admin.site.register(Musical_genre)
admin.site.register(Artist)
