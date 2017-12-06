"""
Urls
"""
from django.conf.urls import include, url
from django.contrib import admin
import website.views
import api.views
from rest_framework_swagger.views import get_swagger_view

admin.autodiscover()

urlpatterns = [
    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
    # Website urls
    url(r'^$', website.views.index, name='index'),
    url(r'^recipes/(?P<recipe_id>[0-9]+)/$', website.views.recipe, name='recipe'),
    # Restful API
    # Following urls define the api
    url(r'^api/$', get_swagger_view(title='Recipes API')),
    url(r'^api/categories/$', api.views.CategoryListView.as_view(), name='category-list'),
    url(r'^api/categories/(?P<category_id>\d+)/recipes/$', api.views.CategoryRecipeListView.as_view(), name='category-recipes-list'),
    url(r'^api/recipes/$', api.views.RecipeListView.as_view(), name='recipe-list'),
    url(r'^api/recipes/(?P<pk>\d+)/$', api.views.RecipeDetailView.as_view(), name='recipe-detail'),
    url(r'^api/recipes/(?P<recipe_id>\d+)/bookmark/$', api.views.RecipeBookmarkView.as_view(), name='recipe-bookmark'),
    url(r'^api/recipes/(?P<recipe_id>\d+)/bookmark/undo$', api.views.RecipeUnbookmarkView.as_view(), name='recipe-unbookmark'),
    url(r'^api/users/$', api.views.UserListView.as_view(), name='user-list'),

]
