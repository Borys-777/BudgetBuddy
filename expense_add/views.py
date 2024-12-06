from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Expense

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

            return redirect('my-login')

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

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'expense_add/my-login.html', context=context)



# Dashboard for registered users

@login_required(login_url='my-login')
def dashboard(request):

    my_expenses = Expense.objects.all()

    context = {'expenses': my_expenses }

    return render(request, 'expense_add/dashboard.html', context=context)


# Create a record 

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            expense = form.save(commit=False)  # Don't save immediately
            expense.user = request.user  # Assign the logged-in user
            expense.save()  # Now save the record with the user
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'expense_add/create-record.html', context=context)


# Update a record 

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'expense_add/update-record.html', context=context)


# View a singular comment 

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Expense.objects.get(id=pk)

    context= {'record': all_records}

    return render(request, 'expense_add/read-record.html', context=context)


# User logout 

def user_logout(request):

    auth.logout(request)

    return redirect('my-login')