from django.urls import path
from . import views

urlpatterns = [    
    path('fuels/', views.fuels, name="fuels"),
    path('fuel/<str:pk>/', views.fuel, name="fuel"),
    path('add-fuel-type/', views.addFuelType, name='add-fuel-type'),
    path('update-fuel/<str:pk>/', views.updateFuel, name='update-fuel'),
    path('delete-fuel/<str:pk>/', views.deleteFuel, name='delete-fuel'),
]