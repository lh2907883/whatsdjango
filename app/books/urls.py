# -*- coding: utf-8 -*- 
# 
from django.conf.urls import patterns, include, url
import app.books.views as views

urlpatterns = patterns('',

    url(r'^index/$', views.IndexAction.as_view()),

    url(r'^findbook/(?P<id>\d*)/?$', views.FindBooksJson.as_view()),
)
