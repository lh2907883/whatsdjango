# -*- coding: utf-8 -*- 
# 
from django.conf.urls import patterns, include, url
import app.books.views as views

urlpatterns = patterns('',

    url(r'^index/$', views.IndexAction.as_view()),

    url(r'^print/$', views.PrintAction.as_view()),
)
