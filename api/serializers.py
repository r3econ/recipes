"""
Serializer classes
"""
from rest_framework import serializers
from django.contrib.auth import models as auth_models
from api import models

class UserGistSerializer(serializers.ModelSerializer):
    """
    Serializer mapping User object into detailed representation
    """

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = auth_models.User
        fields = ('id', 'username')

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer mapping Category objects
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.Category
        fields = ('id', 'name', 'description')

class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer mapping Ingredient objects
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.Ingredient
        fields = ('id', 'name')

class IngredientStepSerializer(serializers.ModelSerializer):
    """
    Serializer mapping IngredientStep objects
    """
    ingredient = IngredientSerializer()

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.IngredientStep
        fields = ('id', 'amount', 'unit', 'ingredient')

class PreparationStepSerializer(serializers.ModelSerializer):
    """
    Serializer mapping PreparationStep objects
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.PreparationStep
        fields = ('id', 'step_number', 'description')

class RecipeGistSerializer(serializers.ModelSerializer):
    """
    Serializer mapping Recipe objects into small (gist) representations
    """
    categories = CategorySerializer(many=True)
    excerpt = serializers.SerializerMethodField()

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.Recipe
        fields = ('id', 'title', 'created_date', 'categories', 'excerpt')

    def get_excerpt(self, obj):
        max_length = 100
        if len(obj.description) <= max_length:
            return obj.description
        else:
            return obj.description[:max_length].rsplit(' ', 1)[0] + '...'

class RecipeDetailSerializer(serializers.ModelSerializer):
    """
    Serializer mapping Recipe objects into detailed representations
    """
    categories = CategorySerializer(many=True)
    ingredient_steps = IngredientStepSerializer(many=True)
    preparation_steps = PreparationStepSerializer(many=True)
    author = UserGistSerializer()

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = models.Recipe
        fields = ('id',
                  'author',
                  'title',
                  'created_date',
                  'description',
                  'preparation_time',
                  'cooking_time',
                  'serving_count',
                  'categories',
                  'ingredient_steps',
                  'preparation_steps')

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer mapping User object into detailed representation
    """
    bookmarked_recipes = RecipeGistSerializer(source='user_profile.bookmarked_recipes', many=True)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        model = auth_models.User
        fields = ('id',
                  'username', 
                  'bookmarked_recipes')