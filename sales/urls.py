from django.urls import path
from . import views

urlpatterns = [    
    path('sales', views.sales, name="sales"),
    path('sale/<str:pk>/', views.sale, name="sale"),
    path('add-sale/', views.addSale, name='add-sale'),        
]