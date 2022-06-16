from inspect import Attribute
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Sale
from . forms import SaleForm

# Create your views here.
@login_required(login_url='login')
def sales(request):    
    sales = Sale.objects.order_by('-date_created')
    # totalamount = Sale.objects.get(volume=33)
    # totalamount.volume = (totalamount.price)*2
    # totalamount.save()
    context = {'sales':sales}    
    return render(request, 'saletemplates/sales.html', context)

@login_required(login_url='login')
def sale(request, pk):
    sale = Sale.objects.get(id=pk)    
    context = {'sale':sale}
    return render(request, 'saletemplates/sale-details.html', context)

@login_required(login_url='login')
def addSale(request):
    form = SaleForm()

    # initial_data = {
    #     'customer_name':'deleted',
    # }

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-sale')
    # else:
    #     form=SaleForm(initial = initial_data)

    context = {'form':form}
    return render(request, 'saletemplates/add-sale-form.html', context)

