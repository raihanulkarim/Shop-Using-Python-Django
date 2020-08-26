from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Car
from django.contrib import messages
# Create your views here.
class HomeListView(ListView):
    model = Car
    template_name = 'items/home.html'
    context_object_name = 'posts'
    paginate_by = 8
    
class ItemDetails(DetailView):
    model = Car
    template_name = 'items/details.html'

class SearchView(ListView):
    model = Car
    template_name = 'items/search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            context = self.model.objects.filter(title__icontains= query)
            if not context:
                context = ''
                messages.warning(self.request, 'No results found!')
        else:
            context = ''
            messages.warning(self.request, 'Insert Keywords to Search Something!')
        return context 

                
