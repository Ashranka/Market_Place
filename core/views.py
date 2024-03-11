from django.shortcuts import redirect, render
from item.models import Category, Item 
from .forms import SignupForm

def index(requets):
    items = Item.objects.filter (is_sold=False)[0:6]
    categories =Category.objects.all()
    return render(requets, 'index.html',{
        'categories': categories,
        'items': items,
    })

def contact (requets):
    return render(requets,'contact.html')

def singup (requets):
    if requets.method == 'POST':
        form = SignupForm(requets.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(requets, 'signup.html',{
        'form': form
    })