import profile
import re
from unittest.mock import seal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from jmespath import search
from shellManagementSystem.decorators import allowed_users
from . models import Fuel
from . forms import FuelForm
from . utils import searchFuels

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fuels(request):

    fuels, search_query = searchFuels(request)

    context = {'fuels':fuels, 'search_query':search_query}
    return render(request, 'fueltemplates/fuels.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fuel(request, pk):
    fuel = Fuel.objects.get(id=pk)    
    context = {'fuel':fuel}
    return render(request, 'fueltemplates/fuel-details.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addFuelType(request):
    form = FuelForm()

    if request.method == 'POST':
        form = FuelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-fuel-type')

    context = {'form':form}
    return render(request, 'fueltemplates/add-fuel-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateFuel(request, pk):
    fuel = Fuel.objects.get(id=pk)
    form = FuelForm(instance=fuel)

    if request.method == 'POST':
        form = FuelForm(request.POST, instance=fuel)
        if form.is_valid():
            form.save()
            return redirect('fuels')

    context = {'form':form}
    return render(request, 'fueltemplates/add-fuel-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteFuel(request, pk):
    fuel = Fuel.objects.get(id=pk) 
    if request.method == 'POST':
        fuel.delete()
        return redirect('fuels')
    context = {'fuel':fuel}
    return render(request, 'fueltemplates/delete-fuel-confirmation.html', context)

