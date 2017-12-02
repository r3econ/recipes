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

class CategoryRecipeListView(generics.ListAPIView):
    """
    API endpoint that returns recipes of a given category.
    """
    serializer_class = serializers.RecipeGistSerializer

    def get_queryset(self):
        """
        Get recipes from a given category
        """
        try:
            category = models.Category.objects.get(id=self.kwargs.get('category_id'))
        except models.Category.DoesNotExist:
            raise exceptions.NotFound('Category not found.')
        return models.Recipe.objects.filter(categories=category)

class RecipeDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows a recipe to be viewed.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer
