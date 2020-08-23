from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserCreateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username},Account Successfully Created!')
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'user/register.html', {'forms':form})
