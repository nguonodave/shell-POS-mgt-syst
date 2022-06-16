from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Employee
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email', 'country', 'job_type']
        widgets = {
            # 'user' : forms.TextInput(attrs={'class':'form-input'}),
            'name' : forms.TextInput(attrs={'class':'form-input'}),
            'email' : forms.TextInput(attrs={'class':'form-input'}),
            'contact' : forms.NumberInput(attrs={'class':'form-input'}),
            'job_type' : forms.Select(attrs={'class':'form-input'}),
            'country' : forms.Select(attrs={'class':'form-input'})
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User        
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})