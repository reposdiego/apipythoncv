from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homepageview(TemplateView):
     template_name = 'core/index.html'
