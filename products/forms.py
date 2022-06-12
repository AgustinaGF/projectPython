from django import forms

class Product_form(forms.Form):
  name = forms.CharField(max_length=40)
  type = forms.CharField(max_length=40)
  price = forms.FloatField()
  description= forms.CharField(max_length=200)
  in_stock = forms.BooleanField()