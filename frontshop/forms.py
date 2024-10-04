# frontshop/forms.py
from django import forms

class OrderForm(forms.Form):
    customer_id = forms.IntegerField(required=True)
    product_id = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True, min_value=1)
    price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
    status = forms.CharField(required=True, max_length=20)