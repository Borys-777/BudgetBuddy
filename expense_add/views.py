from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Expense

# from django.http import HttpResponse
 
class HomePage(TemplateView):
    """
    Displayshomepage"
    """
    template_name = 'expense_add/index.html'

# Create your views here.
# def home(request):
#     return render(request, 'templates_name = index.html')


# Register a user 

def register(request):

    form = CreateUserForm()

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




# User logout 

def user_logout(request):

    auth.logout(request)

    return redirect('my-login')