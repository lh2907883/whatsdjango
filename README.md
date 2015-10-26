# Django 学习笔记

### 一些常用的shell命令


	# 新建项目
	djang-admin.py startproject projectname
	# 新建app
	python manage.py startapp appname
	# 模型建好了之后查看sql
	python manage.py sqlall appname
	# 根据模型同步到数据库
	python manage.py syncdb
	# 在项目上下文执行python代码
	python manage.py shell
	# 在项目数据库环境中执行sql
	python manage.py dbshell
	# 运行项目
	python manage.py runserver 192.168.1.51:3535

### 项目目录结构

* `app` 各个app的代码，app以文件夹名字命名 
* `static` 网站静态资源目录
* `widgets` 一些自定义的widget 