from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home_page(TemplateView):
    template_name = 'home.html'

class about_page(TemplateView):
    template_name = 'about.html'
