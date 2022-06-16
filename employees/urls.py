from django.urls import path
from . import views

urlpatterns = [   
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('register/', views.registerUser, name='register'),


    
    path('employees/', views.employees, name="employees"),
    path('employee/<str:pk>/', views.employee, name="employee"),
    path('add-employee/', views.addEmployee, name='add-employee'),
    path('update-employee/<str:pk>/', views.updateEmployee, name='update-employee'),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name='delete-employee'),
]