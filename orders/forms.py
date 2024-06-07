# 購買表單

from django import forms
from django.forms import inlineformset_factory
from .models import Orders, Orderdetails, Customers, Products

class OrderDetailForm(forms.ModelForm):
    productname = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        label="產品名稱",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantityordered = forms.IntegerField(
        label="購買數量",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Orderdetails
        fields = ['productname', 'quantityordered']

class OrderForm(forms.ModelForm):
    customername = forms.ModelChoiceField(
        queryset=Customers.objects.all(),
        label="客戶名稱",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Orders
        fields = ['customername', 'requireddate', 'status', 'comments']

OrderDetailFormSet = inlineformset_factory(
    Orders, Orderdetails, form=OrderDetailForm,
    fields=['productname', 'quantityordered'], extra=3, can_delete=True
)
