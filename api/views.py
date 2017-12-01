"""
View classes
"""
from rest_framework import generics
from api import models
from api import serializers

class CategoryListView(generics.ListAPIView):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class IngredientListView(generics.ListAPIView):
    """
    API endpoint that allows ingredients to be viewed.
    """
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

class RecipeListView(generics.ListAPIView):
    """
    API endpoint that allows recipes to be viewed.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeGistSerializer

class RecipeDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows a recipe to be viewed.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer
