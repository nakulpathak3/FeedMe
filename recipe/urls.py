from django.conf.urls import patterns, include, url
from django.contrib import admin

from recipe import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipe/$', views.showrecipe, name='showrecipe')
)