from django.db import models

# Create your models here.

class Products(models.Model):
  type:models.CharField(max_length=40)
  price = models.FloatField()
  description = models.CharField(max_length=200, blank=True, null=True)
  in_stock= models.BooleanField(default=True)

  class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Musical_genre(models.Model):
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'genero musical'
        verbose_name_plural = 'generos musicales'

class Artist(models.Model):
    fullname=models.CharField(max_length=50)

    class Meta:
        verbose_name = 'artista'
        verbose_name_plural = 'artistas'
