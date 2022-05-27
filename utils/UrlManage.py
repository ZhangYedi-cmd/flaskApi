#!/usr/bin/python3.6
# @Time    : 2021/8/16 21:12
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : UrlManage.py
# ImakerLab-Website-Flask
import time
from application import app


# Url管理工具类
class UrlManage:

    @staticmethod
    def build_static_url(path):
        version = app.config.get("RELEASE_VERSION")  # 版本号
        ver = "%s" % (int(time.time())) if not version else version  # 如果没有version, 就动态生成时间撮代表版本号
        path = "/static" + path + "?ver=" + ver
        return path

    @staticmethod
    def build_url(path):
        return path
