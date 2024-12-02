from django.contrib import admin
from .models import Expense
from .models import Month

# Register your models here.
admin.site.register(Expense)
admin.site.register(Month)