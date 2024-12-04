from django.shortcuts import render
from django.views.generic import TemplateView

# from django.http import HttpResponse
 
class HomePage(TemplateView):
    """
    Displayshomepage"
    """
    template_name = 'index.html'

# Create your views here.
# def home(request):
#     return render(request, 'templates_name = index.html')
