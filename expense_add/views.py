from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Expense

from django.contrib import messages

# from django.http import HttpResponse
 
class HomePage(TemplateView):
    """
    Displays homepage"
    """
    template_name = 'expense_add/index.html'

# Create your views here.
# def home(request):
#     return render(request, 'templates_name = index.html')


# Register a user 

def register(request):

    # form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully")
            return redirect('my-login')
        else:
            messages.error(request, "Error creating your account")

    else:
        form = CreateUserForm()  # Initialize the form for GET request

    context = {'form':form}
    return render(request, 'expense_add/register.html', context=context)

    # User login 

def my_login(request):
        
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                messages.success(request, "You have logged in")

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'expense_add/my-login.html', context=context)



@login_required(login_url='my-login')
def dashboard(request):
    # Get all expenses for the logged-in user
    my_expenses = Expense.objects.filter(user=request.user)

    # Assuming all expenses have the same currency (for simplicity)
    if my_expenses.exists():
        currency = my_expenses[0].currency  # Get the currency from the first expense
    else:
        currency = 'EUR'  # Default to EUR if no expenses

    context = {
        'expenses': my_expenses,
        'currency': currency,  # Pass the currency to the template
    }
    
    return render(request, 'expense_add/dashboard.html', context=context)


# Create a record 

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            expense = form.save(commit=False)  # Don't save immediately
            expense.user = request.user  # Assign the logged-in user
            expense.currency = 'EUR'  # Ensure the currency is always 'EUR'
            expense.save()  # Now save the record with the user

            messages.success(request, "Your record was created")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'expense_add/create-record.html', context=context)



# Update record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Expense.objects.get(id=pk)

    # Ensure that the logged-in user is the owner of the record
    if record.user != request.user:
        messages.error(request, "You are not authorized to edit this record.")
        return redirect('dashboard')

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            record.currency = 'EUR'  # Ensure the currency is always 'EUR'
            form.save()
            messages.success(request, "Your record was updated")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'expense_add/update-record.html', context=context)


# View a singular comment 

@login_required(login_url='my-login')
def singular_record(request, pk):
    record = Expense.objects.get(id=pk)

    # Ensure that the logged-in user is the owner of the record
    if record.user != request.user:
        messages.error(request, "You are not authorized to view this record.")
        return redirect('dashboard')

    context = {'record': record}
    return render(request, 'expense_add/read-record.html', context=context)



    # Delete record 

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Expense.objects.get(id=pk)

    # Ensure that the logged-in user is the owner of the record
    if record.user != request.user:
        messages.error(request, "You are not authorized to delete this record.")
        return redirect('dashboard')

    record.delete()
    messages.success(request, "Your record was deleted")
    return redirect('dashboard')



# User logout 

def user_logout(request):

    auth.logout(request)

    messages.success(request, "You are logged out")

    return redirect('my-login')



