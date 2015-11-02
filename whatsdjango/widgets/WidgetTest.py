# -*- coding: utf-8 -*- 
from django.forms import TextInput
from django.utils.safestring import mark_safe
from django.utils.html import format_html

class WidgetTest(TextInput):
    # Media内部类定义了这个widget需要的js,css， 其实不仅仅是widget有Media, form也能定义
    class Media:
        # 在页面head元素里面添加 <link href="/static/pretty.css" type="text/css" media="all" rel="stylesheet" /> 
        # /static/ 是在setting里面的STATIC_URL设置的 
        # media="all" 表示这个css适用于所有设备 
        css = {
            'all': ('pretty.css',)
        }
        # 碰到绝对路径就直接引用，不按STATIC_URL设置，<script type="text/javascript" src="http://othersite.com/actions.js"></script>
        js = ('animations.js', 'http://othersite.com/actions.js')
        # extend=false是说不继承基类widget的css和js
        extend = False

    def render(self, name, value, attrs=None):
        # 调用TextInput的render方法得到html(不是普通的字符串类型，是django.utils.safestring.SafeText类型)  
        res = super(TextInput, self).render(name, value, attrs)
        print type(res)

        # 下面两种方式都是构造django.utils.safestring.SafeText的方法，如果直接返回html string，框架会自动htmlencode，导致html代码直接显示到页面上  
        # return mark_safe('<input id="id_address" name="address" type="text" value="火星G-SX1" />')
        return format_html(u'<input id="id_address" name="{}" type="text" value="{}" />', name, value)