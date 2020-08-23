from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Car
# Create your views here.
class HomeListView(ListView):
    model = Car
    template_name = 'items/home.html'
    context_object_name = 'posts'
    paginate_by = 4
    
class ItemDetails(DetailView):
    model = Car
    template_name = 'items/details.html'
