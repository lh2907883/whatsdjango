# coding:utf-8
from django.test import TestCase
from .models import Publisher, Author, Book
from datetime import datetime

# Create your tests here.
# 测试会在创建的临时数据库环境下执行，在测试完毕后临时数据库会被删掉，所有的测试方法必须以test_开头
class BookTestCase(TestCase):

    # 测试启动时调用，并不是测试方法
    def setUp(self):
        # create是创建并保存
        a1 = Author.objects.create(first_name="fn1", last_name="ln1", email="email1@xx.xx")
        a2 = Author.objects.create(first_name="fn2", last_name="ln2", email="email2@xx.xx")
        a3 = Author.objects.create(first_name="fn3", last_name="ln3", email="email3@xx.xx")
        a4 = Author.objects.create(first_name="fn4", last_name="ln4", email="email4@xx.xx")
        a5 = Author.objects.create(first_name="fn5", last_name="ln5", email="email5@xx.xx")
        # 还可以用save保存，其实就是把create拆分为两步，不管是create还是save都会返回这个model对象，可以取到里面的id(主键) 
        a6 = Author(first_name="fn6", last_name="ln6", email="email6@xx.xx")
        a6.save()
        print "a6的id是%d" % a6.id

        p1 = Publisher.objects.create(name="name1", address="address1", city="city1", state_province="state_province1", country="country1", website="http://website1.com")

        b1 = Book(title="title1", publication_date=datetime.now)
        b1.authors.add(a1, a2)
        b1.publisher = p1
        b1.save()

    def test_select_count(self):
        count = Author.objects.all().count()
        self.assertEqual(count, 6)


