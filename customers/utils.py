from django.db.models import Q
from . models import Customer
from countries.models import Country

def searchCustomers(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    country = Country.objects.filter(name__icontains=search_query)

    # customers = Customer.objects.order_by('-date_created')
    customers = Customer.objects.filter(
        Q(username__icontains=search_query) |
        Q(contact__icontains=search_query) |
        Q(customer_status__iexact=search_query) |
        # Q(date_created__icontains=search_query) |        
        Q(country__in=country)        
        ).order_by('-date_created')
    
    return customers, search_query