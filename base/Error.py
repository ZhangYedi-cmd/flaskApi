#!/usr/bin/python3.6
# @Time    : 2021/8/17 0:17
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : Error.py
# ImakerLab-Website-Flask

# 基础错误类型
class BaseErrorMessage:
    Not_Found_Object = {"message": "未查询到相关信息!", "code": "404"}
    DataBase_Error = {"message": "数据库错误!", "code": "500"}
    Message_Lacking = {"message": "填写信息不全!", "code": "404"}
    Server_Error = {"message": "服务器错误!", "code": '500'}
    Redis_Server_Error = {"message": "redis数据库错误!", "code": "500"}
    Has_Already_Reg = {"message": "已经创建过了", "code": '404'}


class LoginErrorMessage(BaseErrorMessage):
    Password_Wrong = {"message": "密码错误!", "code": '404'}
    User_Not_Login = {"message": "密码错误!", "code": '404'}


class TokenErrorMessage(BaseErrorMessage):
    TokenError = {"message": 'token信息错误', "code": "404"}
    Not_Found_Token = {"message": '请求未携带token信息', "code": "404"}
    Login_Out_Time = {"message": '登录过期, 请重新登录', "code": "404"}


class Error:
    def __init__(self, error_message, error_detail):
        self.error_message = error_message
        self.error_detail = error_detail
