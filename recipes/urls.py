from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import website.views

# Examples:
# url(r'^$', 'recipes.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^db', website.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
