from unicodedata import name
from django.forms import ModelForm, Widget
from . models import Fuel
from django import forms

class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = ['name', 'description', 'price', 'fuel_status']
        widgets = {
            'name' : forms.Select(attrs={'class':'form-input'}),
            'description' : forms.Textarea(attrs={'class':'form-input description-input'}),
            'fuel_status' : forms.Select(attrs={'class':'form-input'}),
            'price' : forms.NumberInput(attrs={'class':'form-input'})
        }