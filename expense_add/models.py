from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    """ 
    Model showing the expenses
    """
    # creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100, unique=True, blank=False, default='Indicate your name here')
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

    # created_at = models.DateTimeField(auto_now_add=True) - not sure if this field is required. Will check later

    class Meta:
        ordering = ["id"]

class Month(models.Model):
    """
    Model showing the month of the expenses were made
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
        choices=month_select,  # Used 'choices' instead of 'select'
        # default="January"
    )
    
    year = models.PositiveIntegerField(blank=False, default=2024)  # Changed to PositiveIntegerField

    def __str__(self):
        return f"{self.name} {self.month_name} {self.year}"
