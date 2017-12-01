"""
Model classes
"""
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    """
    Base class for all serializable objects.
    Adds fields used for tracking creation and modification dates.
    """
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        """
        Meta helper class
        """
        abstract = True # Prevent from creating own db table for this class

class Category(BaseModel):
    """
    Recipe category
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        """
        Meta helper class
        """
        verbose_name_plural = "categories"

class Ingredient(BaseModel):
    """
    Recipe ingredient
    """
    name = models.CharField(max_length=100)

class Recipe(BaseModel):
    """
    Recipe
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
