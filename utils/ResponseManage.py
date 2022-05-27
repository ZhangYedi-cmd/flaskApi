#!/usr/bin/python3.6
# @Time    : 2021/8/17 0:34
# @Author  : ZhangYd -- Tust
# @Email   : 178320369@qq.com
# @File    : ResponseManage.py

from flask import jsonify
from flask import make_response
from application import app


class ResponseManage:
    @staticmethod
    def build_json_response(dic):
        return jsonify(dic)

    @staticmethod
    def build_error_response(ErrorObj):
        dic = {
            'error_detail': {
                "error": ErrorObj.error_detail,
                "message": ErrorObj.error_message['message']
            },
            "code": ErrorObj.error_message['code']}
        return jsonify(dic)

    @staticmethod
    def build_token_response(dic, token=None):
        dic['token'] = token
        res = make_response(dic)
        return res
