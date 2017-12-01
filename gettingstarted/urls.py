from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import recipes_website.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', recipes_website.views.index, name='index'),
    url(r'^db', recipes_website.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
