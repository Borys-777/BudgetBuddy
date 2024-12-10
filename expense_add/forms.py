from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Expense

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Create/Register a user here 

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

        # Class for user login 

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Creating a record

class CreateRecordForm(forms.ModelForm):
       
       class Meta:

        model = Expense
        # fields = ['expense_type', 'currency', 'cost'] # this shows the currency input in the form
        fields = ['expense_type', 'cost']
        # exclude = ['currency']


        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     # Make 'currency' field read-only
        #     self.fields['currency'].widget.attrs['readonly'] = True
        #     self.fields['currency'].initial = 'EUR'  # Set initial value to 'EUR'


# Updating a record

class UpdateRecordForm(forms.ModelForm):
       
       class Meta:

        model = Expense
        # fields = ['expense_type', 'currency', 'cost'] # this shows the currency input in the form
        fields = ['expense_type', 'cost']