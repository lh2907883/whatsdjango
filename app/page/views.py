# coding:utf-8
import json
from django.shortcuts import render_to_response
from django.conf.urls import url, patterns
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

class PageAction(View):
    template_name = 'page%s.html'

    def get(self, request, n):
        return render_to_response(self.template_name % n, {})
