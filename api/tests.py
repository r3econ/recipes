"""
Api Tests
"""
from django.urls import reverse
from django.contrib.auth.models import User
from api import models
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

class CategoryTests(APITestCase):
    """
    Category related tests
    """

    def setUp(self):
        """
        Pre-configures testing environment
        """
        # Create users
        self.user = User.objects.create_user(username='user', password='qwerty')

        # Create categories
        self.category_count = 10
        for i in range(0, self.category_count):
            models.Category.objects.create(name='Category {}. name'.format(i)).save()

        # Check the test data
        self.assertEqual(models.Category.objects.count(), self.category_count)
        self.assertEqual(User.objects.count(), 1)

    def test_getting_category_list(self):
        """
        Tests getting category list
        """
        # Authenticate the user
        self.client.force_authenticate(user=self.user)

        # Run the request
        url = reverse('category-list')
        response = self.client.get(url)

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.category_count)

class RecipeTests(APITestCase):
    """
    Recipe related tests
    """

    def setUp(self):
        """
        Pre-configures testing environment
        """
        # Create users
        self.user = User.objects.create_user(username='user', password='qwerty')

        # Create recipes
        self.recipe_count = 10
        for i in range(0, self.recipe_count):
            models.Recipe.objects.create(
                author=self.user,
                title='Recipe {}. name'.format(i),
                description='Test description',
                preparation_time=10,
                cooking_time=20,
                serving_count=5
            ).save()

        # Check the test data
        self.assertEqual(models.Recipe.objects.count(), self.recipe_count)
        self.assertEqual(User.objects.count(), 1)

    def test_getting_recipe_list(self):
        """
        Tests getting recipe list
        """
        # Authenticate the user
        self.client.force_authenticate(user=self.user)

        # Run the request
        url = reverse('recipe-list')
        response = self.client.get(url)

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.recipe_count)

class RecipeBookmarkingTests(APITestCase):
    """
    Recipe related tests
    """

    def setUp(self):
        """
        Pre-configures testing environment
        """
        # Create users
        self.user = User.objects.create_user(username='user', password='qwerty')

        # Create recipes
        self.recipe = models.Recipe.objects.create(
                author=self.user,
                title='Recipe #1',
                description='Test description',
                preparation_time=10,
                cooking_time=20,
                serving_count=5)
        self.recipe.save()

        # Check the test data
        self.assertEqual(models.Recipe.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.user_profile.bookmarked_recipes.count(), 0)

    def test_bookmarking_a_recipe(self):
        """
        Tests bookmarking a recipe
        """
        # Authenticate the user
        self.client.force_authenticate(user=self.user)

        # Run the request
        url = reverse('recipe-bookmark', kwargs={'recipe_id': self.recipe.id, })
        response = self.client.post(url)

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.user_profile.bookmarked_recipes.count(), 1)

    def test_unbookmarking_a_recipe(self):
        """
        Tests undoing bookmarking a recipe
        """
        # Bookmark the recipe
        self.test_bookmarking_a_recipe()

        # Run the request
        url = reverse('recipe-unbookmark', kwargs={'recipe_id': self.recipe.id, })
        response = self.client.post(url)

        # Check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.user_profile.bookmarked_recipes.count(), 0)
