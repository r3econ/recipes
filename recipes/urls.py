from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import website.views
import api.views

# Examples:
# url(r'^$', 'recipes.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
    # Website urls
    url(r'^$', website.views.index, name='index'),
    url(r'^db', website.views.db, name='db'),
    # Restful API
    # Following urls define the api
    url(r'^api/categories/$', api.views.CategoryListView.as_view(), name='category-list'),
    url(r'^api/recipes/$', api.views.RecipeListView.as_view(), name='recipe-list'),
    url(r'^api/recipes/(?P<pk>\d+)/$', api.views.RecipeDetailView.as_view(), name='recipe-detail'),
]
