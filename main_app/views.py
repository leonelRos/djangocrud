from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wish
from .forms import Wish_Form

# Define the home view
def home(request):
    wishes = Wish.objects.all()
    return render(request, 'index.html', {'wishes': wishes})

# def add(request):
#     wishes = Wish.objects.all()
#     return render(request, 'add.html', {'wishes': wishes})

class Add_Wish(CreateView):
  model = Wish
  fields = ['description']

class Delete_Wish(DeleteView):
  model = Wish
  success_url = '/'

