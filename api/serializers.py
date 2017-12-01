"""
Serializer classes
"""
from rest_framework.serializers import ModelSerializer
from api import models
from api import serializers

class CategorySerializer(ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'description', 'created_date')

class IngredientSerializer(ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('id', 'name', 'created_date')

class RecipeGistSerializer(ModelSerializer):

    class Meta:
        model = models.Recipe
        fields = ('id',
                  'title',
                  'description',
                  'created_date')

class RecipeDetailSerializer(ModelSerializer):

    categories = serializers.CategorySerializer(many=True)
    ingredients = serializers.IngredientSerializer(many=True)

    class Meta:
        model = models.Recipe
        fields = ('id',
                  'title',
                  'description',
                  'categories',
                  'ingredients',
                  'created_date')
