from unicodedata import name
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=40,blank=True)
    type = models.CharField(max_length=40, default="CD")
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    in_stock = models.BooleanField(default=True)
    genre = models.ForeignKey('Musical_genre', on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Musical_genre(models.Model):
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'genre musical'
        verbose_name_plural = 'generes musicales'

    def __str__(self):
        return self.genre

class Artist(models.Model):
    fullname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'artista'
        verbose_name_plural = 'artistas'

    def __str__(self):
        return self.fullname
