from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_creation/', views.form_creation),
]