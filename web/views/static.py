#!/usr/bin/python3.6
# @Time    : 2021/8/16 21:16
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : static.py
# ImakerLab-Website-Flask

# 静态文件访问目录
from flask import Blueprint
from flask import send_from_directory
from application import app

static_route = Blueprint("static_route", __name__)


@static_route.route("/<path:filename>")
def return_static_file(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)
