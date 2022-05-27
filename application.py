# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from
from database import *
import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None, static_folder=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=static_folder)
        self.config.from_pyfile('config/base_setting.py')
        self.config.from_pyfile('config/user_settings.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
            # ops_config是选择local|production中的一个
        else:  # 默认运行用线下模型
            self.config.from_pyfile('config/local_setting.py')
        db.init_app(self)


db = SQLAlchemy()

template_folder = os.getcwd() + "/web/templates/"
app = Application(__name__, template_folder=template_folder)  # flask 实例
Swagger(app)  # swagger ui 自动生成接口文档
CORS(app, resources=r'/*')  # 配置跨域
manager = Manager(app)
Migrate(app, db)  # 数据库迁移
manager.add_command('db', MigrateCommand)  # 添加数据库迁移命令
