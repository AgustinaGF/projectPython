from django.contrib import admin
from products.models import Products,Musical_genre,Artist

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display =["name","price","type","description","SKU","in_stock"]

@admin.register(Musical_genre)
class Musical_genreAdmin(admin.ModelAdmin):
  list_display =["genre"]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
  list_display =["fullname"]
