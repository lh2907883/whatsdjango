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

* **whatsdjango/app** 各个app的代码，app以文件夹名字命名 
* **whatsdjango/static** 网站静态资源目录
* **whatsdjango/widgets** 一些自定义的widget 
* **whatsdjango/devstatic** 调试时的静态资源目录(原始js,css代码的存放位置, `grunt export`命令会把静态资源的min版本copy到**whatsdjango/static**供页面使用)
* **grunt** 前端自动化环境根目录(*Gruntfile.js*在这个目录下面)

###环境准备
1. python环境, nodejs环境, grunt-cli
2. 准备grunt环境 
	* cd grunt
    * sudo npm i2. nstall
3. 安装grunt4django
	* sudo pip install grunt4django
4. 项目启动
	* cd whatsdjango
	* python manage.py gruntserver


### 特别主意

1. 由于python是缩进严格的，所以强烈建议打开sublime的 `"translate_tabs_to_spaces": true` 和 `"draw_white_space": "all"` 设置，一定避免tab和空格混搭，否则有意想不到的惊喜噢~