# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

from django.contrib import admin

# 这个函数尝试在每一个已经安装的应用中导入 admin模块. 那些希望被注册使用admin的模块.
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whatsthis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^test1/', include('app.test1.urls')),

    url(r'^books/', include('app.books.urls')),

    # 处理静态资源
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
)
