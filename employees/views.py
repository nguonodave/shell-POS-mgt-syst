from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Employee
from . forms import EmployeeForm


# login view
def loginUser(request):    
    if request.user.is_authenticated:
        return redirect('fuels')

    if request.method == 'POST':
        # setting the username and password
        username = request.POST['username'] # getting the entered value(username) from the form in the browser
        password = request.POST['password'] # getting the entered value(password) from the form in the browser

        try:
            user = User.objects.get(username=username) # the first username is the one in the database(for User model, not form model) the second one is the one in the one above(gotten from the browser)
        except:
            pass
            messages.error(request, 'username dont exist')

        # authenticating if the username matches the password
        user = authenticate(request, username=username, password=password)

        # allowing access to returned page on successful authentication
        if user is not None:
            login(request, user) # using the imported login module to allow access of the loged in employee
            return redirect('fuels')
        else:
            messages.error(request, 'username or pssword is incorrect')
    return render(request, 'employeetemplates/login-register.html')



# logut view
def logoutUser(request):
    logout(request)
    messages.error(request, 'successful logout')
    return redirect('login')



# def registerUser(request):  
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()

#             messages.success(request, 'wowww!')

#     context = {'form':form}
#     return render(request, 'employeetemplates/add-employee-form.html', context)





# employees page view
@login_required(login_url='login')
def employees(request):    
    employees = Employee.objects.order_by('-date_created')
    context = {'employees':employees}    
    return render(request, 'employeetemplates/employees.html', context)

# employees details view
@login_required(login_url='login')
def employee(request, pk):
    employee = Employee.objects.get(id=pk)    
    context = {'employee':employee}
    return render(request, 'employeetemplates/employee-details.html', context)

# @login_required(login_url='login')
# def addEmployee(request):
#     form = EmployeeForm()

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add-employee')

#     context = {'form':form}
#     return render(request, 'employeetemplates/add-employee-form.html', context)


@login_required(login_url='login')
def addEmployee(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'wowww!')

    context = {'form':form}
    return render(request, 'employeetemplates/add-employee-form.html', context)

@login_required(login_url='login')
def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {'form':form}
    return render(request, 'employeetemplates/update-employee-form.html', context)

@login_required(login_url='login')
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk) 
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')
    context = {'employee':employee}
    return render(request, 'employeetemplates/delete-employee-confirmation.html', context)
