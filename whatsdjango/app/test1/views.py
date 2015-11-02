# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request, arg1):
	# assert False #打开注释看看？其实可以看到更多的上下文变量
	print '\033[1;31;40m'
	print arg1
	print '\033[0m'

	return HttpResponse("Hello world " + arg1)

def time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

