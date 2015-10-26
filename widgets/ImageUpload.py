# -*- coding: utf-8 -*- 
from django.forms import Widget
from django.utils.safestring import mark_safe
from django.utils.html import format_html

# 使用inputfile选择图片，然后得到相应的base64编码串，并本地预览，上传
class ImageUpload(Widget):
    class Media:
        js = ('imageupload/imageupload.js', )
        extend = False

    def render(self, name, value, attrs=None):

        return format_html(u'''
            <div class="jq-imgup" style="position:relative;display:inline-block;">
                <img src="{}" alt="没有图片，请选择..">
                <input style="position:absolute;opacity:0;top:0;left:0;width:100%;height:100%;" type="file">
                <input type="hidden" name="{}" value="{}">
            </div>
        ''', value, name, value)

    def value_from_datadict(self, data, files, name):
        # print data[name]
        return data[name]
