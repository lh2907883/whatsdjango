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
        # subject = Publisher.objects.filter(id=subject_id, status=STATUS_ON).first()
        # title = ''
        # if subject:
        #     title = subject.title
        # context = {'title': title, 'track_env': settings.ENV_NAME}
        return render_to_response(self.template_name, {})

class FindBooksJson(View):
    def get(self, request, id=None):
        books = Book.objects
        if id != u'':
            books = books.get(id=id)
        else:
            books = books.all()
        print books


        response = HttpResponse()
        return response