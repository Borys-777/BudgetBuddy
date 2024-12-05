from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CreateUserForm, LoginForm

# from django.http import HttpResponse
 
class HomePage(TemplateView):
    """
    Displayshomepage"
    """
    template_name = 'index.html'

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

            # return redirect('')

    context = {'form':form}

    return render(request, 'expense_add/register.html', context=context)