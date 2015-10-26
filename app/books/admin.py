# -*- coding: utf-8 -*- 
#
from django.db import models
from django.contrib import admin
from django import forms
from app.books.models import Publisher, Author, Book
import datetime
from widgets.WidgetTest import WidgetTest 
from widgets.ImageUpload import ImageUpload 

# 这是一个admin里面用的form，继承django.forms.ModelForm
class AuthorAdminForm(forms.ModelForm):
    photo = forms.CharField(widget=ImageUpload())

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'fullname', 'email', 'photo') #fullname是个自定义的字段，就是在AuthorModel里面定义的一个方法
    search_fields = ('first_name', 'last_name')
    form = AuthorAdminForm

class BookAdmin(admin.ModelAdmin):
    #获取action时调用（删掉默认的删除行为）（其实你可以做的更多，比如根据不同用户生成不同的行为）
    def get_actions(self, request):
        actions = super(BookAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions 

    #admin保存时调用（注意，并非BookModel保存调用，如果想要达到这个效果，可以设置BookModel的save方法）
    #ModelAdmin里面有各种钩子方法,详见(http://python.usyiyi.cn/django/ref/contrib/admin/index.html#modeladmin-methods)
    def save_model(self, request, obj, form, change):
        obj.publication_date = datetime.datetime.now()
        obj.save()

    def make_statues(self, request, queryset):
        queryset.update(status=1)
    make_statues.short_description = u"出版选中的书籍"

    list_display = ('title', 'publisher', 'publication_date', 'status') #显示的字段
    list_filter = ('publication_date',) #一般用在datetime,bool类型上，一个简单的筛选
    date_hierarchy = 'publication_date' 
    search_fields = ('title', 'publisher') #搜索框要搜索的字段
    ordering = ('-publication_date',) #数据的排序规则（按publication_date倒序）
    fields = ('title', 'authors', 'publisher', 'status') #编辑的字段（只编辑写了的，如果不设置就是所有字段都编辑）
    # exclude = ('publication_date',) #exclude和fields正好相反，表示除publication_date以外的字段都能编辑
    filter_horizontal = ('authors',) #使authors按照（两个多选列表的水平排列方式）编辑，只能用在多对多字段，还有垂直排列噢（用filter_vertical）
    raw_id_fields=('publisher',) #一对多的外键字段默认使用下拉框显示，但是如果下拉列表很多时可以用raw_id_fields制定用文本框显示，手动输入id（有搜索按钮告诉你出版社的id）
    actions = [make_statues] #定义行为（默认有个删除的行为）,触发时调用make_statues方法

# 这是一个admin里面用的form，继承django.forms.ModelForm
class PublisherAdminForm(forms.ModelForm):
    address = forms.CharField(widget=WidgetTest())

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    # admin详情页里面可以分组显示
    fieldsets = (
        (None, {'fields': ('name',)}),
        (u'地址', {'fields': ('address', 'city', 'state_province', 'country')}),
        (u'其他', {'fields': ('website',), 'classes': ('collapse',)}),
    )
    # form可以指定一个表单，在表单里面可以定制字段的显示方式(widget)和验证 
    form = PublisherAdminForm

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)