"""
Website views
"""
from django.shortcuts import render
from api import models

def index(request):
    """
    Home page
    """
    recipes = models.Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipes(request):
    """
    Recipe list
    """
    recipes = models.Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})
