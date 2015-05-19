from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([0-9]+)$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^success/$', views.success, name='success'),
]