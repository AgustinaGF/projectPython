# Generated by Django 4.0.4 on 2022-07-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
