from django.db.models import Q
from . models import Fuel

def searchFuels(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')        

    # fuels = Fuel.objects.order_by('-date_created')
    fuels = Fuel.objects.filter(
        Q(name__icontains=search_query) |
        Q(fuel_status__iexact=search_query)
        ).order_by('-date_created')
    
    return fuels, search_query