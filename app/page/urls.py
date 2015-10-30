# -*- coding: utf-8 -*- 
# 
from django.conf.urls import patterns, include, url
import app.page.views as views

urlpatterns = patterns('',

    url(r'^p(?P<n>[\d]+)/$', views.PageAction.as_view()),

    # url(r'^print/$', views.PrintAction.as_view()),
)
