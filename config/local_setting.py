# -*- coding: utf-8 -*-
# 是否开启debug模式
DEBUG = True

# sqlalchemy ==> mysql
username = ""  # set your mysql username
pwd = ""  # set your mysql password
database_name = ""  # set your mysql database


SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{pwd}@127.0.0.1:3306/{database_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8"

# redis 配置
REDIS_PORT = 6379
REDIS_HOST = "127.0.0.1"
REDIS_DATABASE_INDEX = 0

# 忽略token的url
IGNORE_URLS = []
