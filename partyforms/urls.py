from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form_response/', include('form_response.urls')),
]
