# Generated by Django 4.0.4 on 2022-07-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]