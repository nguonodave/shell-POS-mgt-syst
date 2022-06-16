from django.forms import ModelForm
from . models import Customer
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'contact', 'email', 'country', 'customer_status']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-input'}),
            'last_name' : forms.TextInput(attrs={'class':'form-input'}),
            'username' : forms.TextInput(attrs={'class':'form-input'}),
            'email' : forms.TextInput(attrs={'class':'form-input'}),
            'contact' : forms.NumberInput(attrs={'class':'form-input'}),
            'customer_status' : forms.Select(attrs={'class':'form-input'}),
            'country' : forms.Select(attrs={'class':'form-input'})
        }