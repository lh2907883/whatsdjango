# -*- coding: utf-8 -*- 

from django.db import models
from django.utils.html import format_html

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    # 类似ToString方法
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'出版社'
        verbose_name = u'出版社'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    photo = models.TextField(null=True,blank=True)

    def fullname(self):
        #print isinstance(self.first_name, unicode)
        return format_html(u'<span style="color: red;">{} {}</span>', self.first_name, self.last_name)

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = u'作者'
        verbose_name = u'作者'

class Book(models.Model):
    BOOK_STATUS = (
        (0, '未出版'),
        (1, '已出版'),
    )

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    status = models.IntegerField(default=0,choices=BOOK_STATUS) #类似枚举

    #book模型的保存钩子
    #在Python中* 和 ** 有特殊含义，他们与函数有关，在函数被调用时和函数声明时有着不同的行为。此处*号不代表C/C++的指针。其中 * 表示的是元祖或是列表，而 ** 则表示字典
    def save(self, *args, **kwargs):
        print 'book saved'
        super(Book, self).save(*args, **kwargs) #调用基类真正的保存

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = u'书'
        verbose_name = u'书'
