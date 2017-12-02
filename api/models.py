"""
Model classes
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class BaseModel(models.Model):
    """
    Base class for all serializable objects.
    Adds fields used for tracking creation and modification dates.
    """
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta: # pylint: disable=too-few-public-methods
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

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'Category #{}: {}'.format(self.id, self.name)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta helper class
        """
        verbose_name_plural = "categories"

class Ingredient(BaseModel):
    """
    Recipe ingredient
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'Ingredient #{}: {}'.format(self.id, self.name)

class Recipe(BaseModel):
    """
    Recipe
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='recipes')
    preparation_time = models.IntegerField(null=True, help_text="Preparation time in minutes")
    cooking_time = models.IntegerField(null=True, help_text="Cooking time in minutes")
    serving_count = models.IntegerField(default=1)

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'Recipe #{}: {}'.format(self.id, self.title)

class PreparationStep(BaseModel):
    """
    Preparation step. Description what to do when cooking.
    """
    step_number = models.IntegerField()
    description = models.TextField(null=False, blank=False)
    recipe = models.ForeignKey(Recipe, related_name='preparation_steps', on_delete=models.CASCADE)

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'PreparationStep #{}: {}. - {}'.format(self.id, self.step_number, self.description)

class IngredientStep(BaseModel):
    """
    Ingredient step. Information about the amount
    of the ingredient in the recipe.
    """
    recipe = models.ForeignKey(Recipe, related_name='ingredient_steps', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount = models.FloatField()
    unit = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'IngredientStep #{}: {} - {} {}'.format(self.id, self.ingredient, self.amount, self.unit)

class UserProfile(BaseModel):
    """
    User Profile extends the built-in User class adding
    profile related fields.
    """
    user = models.OneToOneField(User, related_name='user_profile')
    bookmarked_recipes = models.ManyToManyField(Recipe, blank=True, related_name='bookmarked_by')

    def __str__(self):
        """
        Informal string representation of the instance
        """
        return 'UserProfile #{}: User({}, {})'.format(self.id, self.user.id, self.user.username)
    
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Creates user profile when User object is created
        """
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)