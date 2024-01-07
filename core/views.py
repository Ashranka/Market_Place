from django.shortcuts import render


def index(requets):
    return render(requets, 'index.html')
