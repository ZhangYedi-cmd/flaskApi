# Flask应用开发模板

## ✨特性

+ 开箱即用
+ 整合好Flask常见库，直接开发
+ 规范的代码结构
+ 封装常用的工具类

## 🔧 技术选型

+ Flask
+ flask_sqlalchemy  迁移数据库
+ flasgger  生成swagger 接口文档
+ flask_cors 配置跨域
+ flask_migrate flask命令行工具

## 📦 项目目录

base 响应信息

config 配置文件

docs swagger ui生成接口文档

utils 常用工具封装（token生成，密码加密，Redis连接工具）

jobs 存放定时任务

web 

+ models 实体类
+ staic 静态资源
+ templates 模板文件
+ views 视图函数

application.py  初始化的flask实例，为其做各种库的配置

database.py  实体类迁移统一配置

manager.py  flask命令

www.py 蓝图注册

RunProject 快捷启动项目

## 🔥快速上手

在views中新建一个py文件，创建蓝图来写你的视图函数。 

```python
from flask import Blueprint
from flask import render_template

route_index = Blueprint('index_page', __name__)


@route_index.route("/index")
def index():
    # return "ok!"
    # return redirect('http://www.baidu.com')
    return render_template("index.html")
```

写好视图函数后，将蓝图注册到www.py

```python
from web.views.index import route_index
from application import app

# 注册蓝图
app.register_blueprint(route_index)
```

恭喜你，视图函数就已经配置好了！

随后，打开终端启动项目吧！

```shell
python manager.py runserver
或
python RunProject.py
```



## 🛡数据库配置

### 配置基础信息

在/config/local_setting.py 中配置数据库信息

```python
# sqlalchemy ==> mysql
username = ""  # set your mysql username
pwd = ""  # set your mysql password
database_name = ""  # set your mysql database
```

### 数据库迁移操作

1. 在/web/models中写好实体类 

2. 将写好的实体类导入到database.py中

3. 打开终端， 依次输入一下命令

   ```shell
   python manage.py db init  # 第一次迁移时输入即可，之后迁移不需要再输入
   python manage.py db migrate 
   python manage.py db upgrade
   ```

## 项目部署

参考我的博客：[Flask项目部署教程](http://49.232.14.242/blog/webProjectServer/Flask+Vue/#vue-flask-uwsgi-nginx-%E9%83%A8%E7%BD%B2)

如果本仓库对你有帮助，求star⭐。 
