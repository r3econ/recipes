"""
View classes
"""
from rest_framework import generics
from rest_framework import exceptions
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
from api import serializers

class CategoryListView(generics.ListAPIView):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

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

class RecipeBookmarkView(APIView):
    """
    post: Bookmarks the recipe
    """
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        """
        Bookmarks the recipe
        """
        # Get the recipe
        try:
            recipe = models.Recipe.objects.get(id=kwargs.get('recipe_id'))
        except models.Recipe.DoesNotExist:
            raise exceptions.NotFound('Recipe not found.')

        if request.user.user_profile.bookmarked_recipes.filter(id=recipe.id).exists():
            # User already bookmarked
            return Response('Recipe already bookmarked', status=status.HTTP_409_CONFLICT)
        else:
            # Bookmark the recipe
            request.user.user_profile.bookmarked_recipes.add(recipe)
            return Response(status=status.HTTP_200_OK)

class RecipeUnbookmarkView(APIView):
    """
    post: Undoes bookmarking of the recipe
    """
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        """
        Unbookmarks the recipe
        """
        # Get the recipe
        try:
            recipe = models.Recipe.objects.get(id=kwargs.get('recipe_id'))
        except models.Recipe.DoesNotExist:
            raise exceptions.NotFound('Recipe not found.')

        # User already follows.
        if request.user.user_profile.bookmarked_recipes.filter(id=recipe.id).exists():
            # Remove recipe from bookmarks
            request.user.user_profile.bookmarked_recipes.remove(recipe)
            return Response(status=status.HTTP_200_OK)
        else:
            # User is not following this entry
            return Response("Recipe not bookmarked. Can't unbookmark.", status=status.HTTP_409_CONFLICT)
