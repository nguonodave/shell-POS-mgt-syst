from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shellManagementSystem.decorators import allowed_users
from . models import Customer
from . forms import CustomerForm
from . utils import searchCustomers

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request): 

    customers, search_query = searchCustomers(request)

    # guest = Customer.objects.get(customer_status=2)
    # guest.username = "guest"
    # guest.save()
    context = {'customers':customers, 'search_query':search_query}    
    return render(request, 'customertemplates/customers.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)    
    context = {'customer':customer}
    return render(request, 'customertemplates/customer-details.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-customer')

    context = {'form':form}
    return render(request, 'customertemplates/add-customer-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {'form':form}
    return render(request, 'customertemplates/add-customer-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk) 
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    context = {'customer':customer}
    return render(request, 'customertemplates/delete-customer-confirmation.html', context)
