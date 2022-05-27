#!/usr/bin/python3.6
# @Time    : 2021/8/24 9:53
# @Author  : ZhangYd -- Turedis_cli
# @Email   : 178320369@qq.com
# @File    : __init__.py.py
# ImakerLab-Website-Flask

from redis import *
from application import app


class Redis:
    inner_obj = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.inner_obj:
            obj = object.__new__(cls)
            obj.redis_cli = StrictRedis(
                host=app.config["REDIS_HOST"],
                port=app.config['REDIS_PORT'],
                db=3
            )
            cls.inner_obj = obj
            return obj
        else:
            return cls.inner_obj

    # 通过反射将对象模拟成一个字典来操作
    def __getitem__(self, item):
        res = self.redis_cli.get(item)
        return res

    def __setitem__(self, key, value):
        self.redis_cli.set(key, value)

    def __delitem__(self, item):
        self.redis_cli.delete(item)

    def item_is_exists(self, item):
        res = self.redis_cli.exists(item)
        return res
