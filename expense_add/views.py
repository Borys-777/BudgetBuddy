from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displayshomepage"
    """
    template_name = 'index.html'

# Create your views here.
