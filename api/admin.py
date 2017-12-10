"""
Admin interface
"""
from django.contrib import admin
from api import models

class UserProfileAdmin(admin.ModelAdmin):
    """
    UserProfile admin interface
    """
    fields = ['id', 'bookmarked_recipes', 'user']
    readonly_fields = ['id']
    list_display = ['id', 'user']
    search_fields = ['id']

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
              'preparation_time', 'serving_count', 'categories', 
              'preparation_info', 'ingredient_info']
    readonly_fields = ['id']
    list_display = ['title', 'author', 'id']
    search_fields = ['title', 'description']

# Register admin interfaces
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
