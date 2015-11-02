# coding:utf-8
from django.test import TestCase
from .models import Publisher, Author, Book
import datetime as dt

# Create your tests here.
# 测试会在创建的临时数据库环境下执行，在测试完毕后临时数据库会被删掉，所有的测试方法必须以test_开头
class BookTestCase(TestCase):

    # 在每一个测试方法启动时调用，并不是测试方法
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
        p2 = Publisher.objects.create(name="name2", address="address2", city="city2", state_province="state_province2", country="country2", website="http://website2.com")
        p3 = Publisher.objects.create(name="name3", address="address3", city="city3", state_province="state_province3", country="country3", website="http://website3.com")

        now = dt.datetime.now()
        b1 = Book(title="title1", publication_date=now)
        b1.publisher = p1
        b1.save()
        # 多对多的字段必须在model更新到数据库之后在再添加关系才行，否则会报错，而外键字段（例如上面的publisher必须在save之前赋值，因为有数据库约束）
        b1.authors.add(a1, a2)

        b2 = Book.objects.create(title="title2", publication_date=now-dt.timedelta(days=1), publisher=p2)
        b2.authors.add(a2, a4, a6)
        b3 = Book.objects.create(title="title3", publication_date=now, publisher=p2)
        b3.authors.add(a3, a4, a5, a6)
        b4 = Book.objects.create(title="title4", publication_date=now+dt.timedelta(days=1), publisher=p3)
        b4.authors.add(a1, a2, a6)


    def test_select(self):
        # 查询所有
        res1 = Author.objects.all()
        self.assertEqual(res1.count(), 6)
        # 取0到6条(不包括6),间隔为2的记录, #a1,a3,a5
        self.assertEqual(len(res1[0:6:2]), 3)

        # 精确查找
        res2 = Author.objects.filter(first_name="fn3")
        self.assertEqual(res2.count(), 1)

        # 字段查找 例子:like '%5%'
        # 查询条件是通过『字段__条件函数』作为filter参数传递的，所以关键就是要知道"条件参数"，下面列出常用的
        # iexact        忽略大小写的等于
        # contains      包含              like '%xxx%'
        # icontains     忽略大小写的包含
        # gt            大于              > 4
        # gte           大于等于           >= 4
        # lt            小于              < 4
        # lte           小于等于           <= 4
        # range         在xx和xxx之间      between xx and xxx       .filter(field__range=(3,10)) 
        # startswith    开始于            like '%xxx'
        # istartswith
        # endswith      结束于            like 'xxx%'
        # iendswith
        # isnull        等于空             is null                  .filter(field__isnull=True)
        # regex         满足正则                                    .filter(field__regex=r'^(An?|The)+')
        # iregex
        res3 = Author.objects.filter(email__contains="5")   #a5
        self.assertEqual(res3.count(), 1)

        # in查询, in子查询
        res4 = Author.objects.filter(first_name__in=["fn1", "fn2", "fn5"])   #a1, a2, a5
        self.assertEqual(res4.count(), 3)
        plist = Publisher.objects.filter(name__in=["name1", "name2"])
        res5 = Book.objects.filter(publisher__in=plist)     #b1, b2, b3
        self.assertEqual(res5.count(), 3)

        # 关联查询
        # 查询名字为name2的出版社出版的所有书, 结果是[b2, b3]
        res6 = Book.objects.filter(publisher__name="name2")
        self.assertEqual(res6.count(), 2)
        # 查询名字为fn2的作者写了哪些书，结果是[b1, b2, b4]
        res7 = Book.objects.filter(authors__first_name="fn2")
        self.assertEqual(res7.count(), 3)
        # 反过来也可以~ 查询名字为title2的书的作者有哪些，结果是[a2, a4, a6]
        res8 = Author.objects.filter(book__title="title2")
        self.assertEqual(res8.count(), 3)

















