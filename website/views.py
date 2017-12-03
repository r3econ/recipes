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

def recipe(request, recipe_id):
    """
    Recipe list
    """
    recipe = models.Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe.html', {'recipe': recipe})
