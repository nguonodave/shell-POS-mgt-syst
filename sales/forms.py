from django.forms import ModelForm
from . models import Sale
from django import forms

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['customer_name', 'fuel', 'price', 'volume', 'total_price', 'amount_paid', 'balance', 'served_by']
        widgets = {
            'customer_name' : forms.Select(attrs={'class':'form-input sale-form-input'}),
            'fuel' : forms.Select(attrs={'class':'form-input sale-form-input'}),
            'price' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'volume' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),            
            'total_price' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'amount_paid' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'balance' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'served_by' : forms.Select(attrs={'class':'form-input sale-form-input'})
        }