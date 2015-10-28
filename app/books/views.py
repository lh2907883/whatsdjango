# coding:utf-8
import json
from django.shortcuts import render_to_response
from django.conf.urls import url, patterns
from django.conf import settings
from django.views.generic import View
from app.books.models import Publisher, Book
from django.http import HttpResponse

# Create your views here.

class IndexAction(View):
    # 安装过的app(在INSTALLED_APPS里有注册)的模板都放在app的templates目录下，这是约定，不要问为什么 
    template_name = 'index.html'

    def get(self, request):
        return render_to_response(self.template_name, {})

class PrintAction(View):
    def get(self, request):
        res = 'Print request.COOKIES: <br>'
        for k, v in request.COOKIES.items():
            res += 'key: %s; value: %s <br>' % (k, v)

        res += 'Print request.session: <br>'
        for k, v in request.session.items():
            res += 'key: %s; value: %s <br>' % (k, v)

        response = HttpResponse(res)
        return response