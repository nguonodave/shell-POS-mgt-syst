from django.urls import path
from . import views

urlpatterns = [    
    path('customers/', views.customers, name="customers"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('add-customer/', views.addCustomer, name='add-customer'),
    path('update-customer/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),
]