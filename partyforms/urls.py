from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^create_form/', include('create_form.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
