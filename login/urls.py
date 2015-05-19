from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth', views.auth),
    url(r'^logout', views.sign_out),
]