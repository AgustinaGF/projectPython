# Generated by Django 4.0.5 on 2022-06-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.CharField(default='CD', max_length=40),
        ),
    ]
