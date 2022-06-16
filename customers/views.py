from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Customer
from . forms import CustomerForm

# Create your views here.
@login_required(login_url='login')
def customers(request):    
    customers = Customer.objects.order_by('-date_created')
    # guest = Customer.objects.get(customer_status=2)
    # guest.username = "guest"
    # guest.save()
    context = {'customers':customers}    
    return render(request, 'customertemplates/customers.html', context)

@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)    
    context = {'customer':customer}
    return render(request, 'customertemplates/customer-details.html', context)

@login_required(login_url='login')
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
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk) 
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    context = {'customer':customer}
    return render(request, 'customertemplates/delete-customer-confirmation.html', context)
