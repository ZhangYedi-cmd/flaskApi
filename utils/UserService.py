#!/usr/bin/python3.6
# @Time    : 2021/8/16 21:20
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : UserService.py
# ImakerLab-Website-Flask
import hashlib
import string
import random
import datetime
from hashlib import md5
import base64


class UserService:
    # 产生邮件验证码
    @staticmethod
    def get_email_code(length=6):
        code = "".join([random.choice((string.ascii_letters + string.digits)) for i in range(length)])
        return code

    # 用于前端cookie
    @staticmethod
    def gene_auth_code(user_info=None):
        # 产生授权码
        m = md5()  # 首先创建一个md5加密对象
        str = "%s-%s-%s-%s" % (user_info.uid, user_info.username, user_info.password, user_info.salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()  # 转换为16进制

    # 获取salt密钥
    @staticmethod
    def get_random_salt(length=16):
        key = "".join([random.choice((string.ascii_letters + string.digits)) for i in range(length)])
        return key

    # 加密
    @staticmethod  # 随机生成的密钥 + 用户输入密码 进行base64加密
    def encrypt_str(password, salt):
        m = md5()
        code = "%s-%s" % (base64.encodebytes(password.encode("utf-8")), salt)
        m.update(code.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def check_not_null(field_list, dic):
        # 传入对象非空校验
        print("非空列表:", field_list)
        for item in field_list:
            if item not in dic or dic[item] == '':
                print("空值", item)
                return False
        return True

    @staticmethod
    def get_time(utc_time):
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        return datetime.datetime.strptime(utc_time, UTC_FORMAT)


class UserDataBaseService:
    pass
