from django.shortcuts import render
from item.models import Category, Item 

def index(requets):
    items = Item.objects.filter (is_sold=False)
    return render(requets, 'index.html')

def contact (requets):
    return render(requets,'contact.html')
