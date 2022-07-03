from django.db.models import Q
from . models import Sale
from customers.models import Customer
from fuels.models import Fuel
from employees.models import Employee

def searchSales(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    customer = Customer.objects.filter(username__icontains=search_query)
    fuel = Fuel.objects.filter(name__icontains=search_query)
    employee = Employee.objects.filter(user__username__icontains=search_query)

    # sales = Sale.objects.order_by('-date_created')
    sales = Sale.objects.filter(
        Q(customer_name__in=customer) |
        Q(fuel__in=fuel) |
        Q(date_created__icontains=search_query) |
        Q(served_by__in=employee)        
        ).order_by('-date_created')
    
    return sales, search_query