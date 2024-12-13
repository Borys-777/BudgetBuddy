from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    """ 
    Model showing the expenses
    """
    # creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=100, unique=True, blank=False, default='Type your expenses here')

    # To be implemented in the next sprint (lack of time)
    # currency_select = [
    #     # ('USD', 'USD'),
    #     # ('GBP', 'GBP'),
    #     ('EUR', 'EUR'),
    # ]
    currency = models.CharField(
        max_length=3,
        default='EUR'
       
    )

    cost = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        ordering = ["id"]

class Month(models.Model):
    """
    Model showing the month of the expenses were made. It is shown in admin panel, but I will implement it for the next sprint. Lack of time for now.
    """
    month_select = [
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"), 
        ("May", "May"), 
        ("June", "June"), 
        ("July", "July"), 
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),  
        ("November", "November"),
        ("December", "December"),
    ]
    
    month_name = models.CharField(
        max_length=12,
        choices=month_select,  
        
    )