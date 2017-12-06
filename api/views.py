"""
Views
"""
from rest_framework import generics
from rest_framework import exceptions
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
from api import serializers
import api.permissions

class CategoryListView(generics.ListAPIView):
    """
    Returns list of categories
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class RecipeListView(generics.ListAPIView):
    """
    Returns a list of recipes
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeGistSerializer

class CategoryRecipeListView(generics.ListAPIView):
    """
    Returns recipes of a given category
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

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get: Returns recipe details
    patch: Updates recipe details
    put: Replaces the recipe
    delete: Deletes the recipe
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer
    permission_classes = (api.permissions.IsAuthorOrReadOnly, )

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

        # User is not following this entry
        return Response("Recipe not bookmarked. Can't unbookmark.", status=status.HTTP_409_CONFLICT)
