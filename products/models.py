from unicodedata import name
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=40,blank=True)
    type = models.CharField(max_length=40, default="CD")
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Musical_genre(models.Model):
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'genre musical'
        verbose_name_plural = 'generes musicales'


class Artist(models.Model):
    fullname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'artista'
        verbose_name_plural = 'artistas'
