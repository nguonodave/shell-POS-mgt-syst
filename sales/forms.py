from faulthandler import disable
from tkinter import DISABLED
from django.forms import ModelForm
from . models import Sale
from django import forms
from django.contrib.auth.models import User

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['customer_name', 'fuel', 'price', 'volume', 'total_price', 'amount_paid', 'balance', 'served_by']
        
        user = User.objects.get(username='scottcannon')

        # def my_view(request):
        #     user = None
        #     if request.user.is_authenticated():
        #         user = request.user.username
        #     print(user)

        widgets = {
            'customer_name' : forms.Select(attrs={'class':'form-input sale-form-input'}),
            'fuel' : forms.RadioSelect(attrs={'class':'radio-inputs'}),
            'price' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'volume' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),            
            'total_price' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'amount_paid' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'balance' : forms.NumberInput(attrs={'class':'form-input sale-form-input'}),
            'served_by' : forms.TextInput(attrs={
                'class':'form-input sale-form-input',
                'value':user,
                # DISABLED: True
                })
        }