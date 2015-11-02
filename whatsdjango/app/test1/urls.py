# -*- coding: utf-8 -*- 
# 第一行是说源文件以utf-8的形式编码保存，不然python会报错
from django.conf.urls import patterns, include, url
#from view import hello
from app.test1.views import time

urlpatterns = patterns('',

    url(r'^^hello/([^/]*)/?$', 'app.test1.views.hello'),

    url(r'^time/$', time),
)
