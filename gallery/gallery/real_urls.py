from django.conf.urls.defaults import *
from django.conf.urls.defaults import include, patterns,url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	url(r'^', include('gallery.items.urls')),
)