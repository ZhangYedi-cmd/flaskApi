#!/usr/bin/python3.6
# @Time    : 2021/8/24 11:07
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : TokenService.py
# ImakerLab-Website-Flask
from utils.Redis_client import Redis
from base.Error import *


class TokenService:
    redis_cli = Redis()

    @classmethod
    def set_token(cls, token, user_info=None):
        try:
            cls.redis_cli[user_info.username] = token
            return True
        except Exception as e:
            return Error(BaseErrorMessage.Redis_Server_Error, str(e))

    @classmethod
    def get_token(cls, user_info=None):
        try:
            return cls.redis_cli[user_info.username]
        except Exception as e:
            print(e)
            return Error(BaseErrorMessage.Redis_Server_Error, str(e))

    @classmethod
    def delete_token(cls, user_info=None):
        try:
            del cls.redis_cli[user_info.username]
            return True
        except Exception as e:
            return Error(BaseErrorMessage.Redis_Server_Error, str(e))
