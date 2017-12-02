"""
Admin interface
"""
from django.contrib import admin
from api import models

class IngredientAdmin(admin.ModelAdmin):
    """
    Ingredient admin interface
    """
    fields = ['id', 'name']
    readonly_fields = ['id']
    list_display = ['name', 'id']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin interface
    """
    fields = ['id', 'name', 'description']
    readonly_fields = ['id']
    list_display = ['name', 'id']
    search_fields = ['name', 'description']

class RecipeAdmin(admin.ModelAdmin):
    """
    Recipe admin interface
    """
    fields = ['id', 'title', 'description', 'author', 'cooking_time',
              'preparation_time', 'serving_count']
    readonly_fields = ['id']
    list_display = ['title', 'author', 'id']
    search_fields = ['title', 'description']

# Register admin interfaces
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
