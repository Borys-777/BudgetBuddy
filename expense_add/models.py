from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Expense (models.Model):
    """ 
    Model showing the expenses
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=100, unique=True, blank=False, default='Type your expenses here') 
    currency_select = [
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
    ]
    currency = models.CharField(
        max_length=3,
        choices=currency_select,
        default='EUR'
        )

    cost = models.DecimalField(
        max_digits=7,
        decimal_places=2
        )

class Month (models.Model): 

    """
    Model showing the month of the expenses were made
    """
    month_select [
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"), 
        ("May", "May"), 
        ("June", "June"), 
        ("July", "July"), 
        ("August", "August"),
        ("September", "September"),
        ("October", "OCtober"), 
        ("November", "November"),
        ("December", "December"),
    ]

    month_name = models.CharField(
        max_length=12,
        choices=month_select,
    )

    year = models.CharField(blank=False, default = "2024")

    def __str__(self):
        return self.year
