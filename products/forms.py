from django import forms
from products.models import Products


class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
