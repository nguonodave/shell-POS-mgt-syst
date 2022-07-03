from django.db.models import Q
from . models import Employee
from countries.models import Country

def searchEmployees(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    country = Country.objects.filter(name__icontains=search_query)

    # employees = Employee.objects.order_by('-date_created')
    employees = Employee.objects.filter(
        Q(name__icontains=search_query) |
        Q(contact__icontains=search_query) |
        # Q(date_created__icontains=search_query) |
        Q(job_type__icontains=search_query) |
        Q(country__in=country)
        ).order_by('-date_created')
    
    return employees, search_query