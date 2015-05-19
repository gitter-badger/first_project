from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event_list/$', views.event_list, name='event_list'),
    url(r'^$', views.index, name='index'),

]