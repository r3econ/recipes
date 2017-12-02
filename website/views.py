"""
Website views
"""
from django.shortcuts import render
from api import models

def index(request):
    """
    Home page
    """
    return render(request, 'index.html')

def recipes(request):
    """
    Recipe list
    """
    recipes = models.Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})
