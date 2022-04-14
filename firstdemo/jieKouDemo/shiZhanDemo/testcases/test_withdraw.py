# -*- coding: utf-8 -*-
# author：slz time:2022/4/2
'''
'''
import unittest
import os

import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from ..common.handle_excel import HandleExcel
from ..common.handle_path import DATA_DIR
from ..common.handle_conf import conf
from ..common.handler_log import my_log


@ddt
class TestWithdraw(unittest.TestCase):
    execl = HandleExcel(os.path.join(DATA_DIR, "apicases.xlsx"), 'withdraw')
    cases = execl.read_data()

    @classmethod
    def setUpClass(cls):
        url = conf.get('env', 'base_url' + '/member/login')
        params = {
            "mobile_phone": conf.get("test_data", "mobile"),
            "pwd": conf.get("test_data", "pwd")
        }
        headers = eval(conf.get("env", "headers"))
        res = requests.post(url=url, json=params, headers=headers).json()
        # 登录之后提取token
        token = jsonpath(res, '$..token')[0]
        # 将token添加到请求头
        headers["Authorization"] = "Bearer" + token
        # 保存含有token的请求头为类属性
        # setattr(TestRecharge,"headers",headers)
        cls.headers = headers

        # 提取用户的id给充值接口使用
        cls.member_id = jsonpath(res, '$..id')[0]

    @list_data(cases)
    def test_withdraw(self, item):
        url = conf.get("env", "base_url") + item['url']
        # 动态处理需要替换的参数
        item['data'] = item["data"].replace("#member_id#", str(self.member_id()))

        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()

        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()

        # 断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e :
            my_log.error("用例---【{}】---执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---【{}】---执行成功".format(item['title']))
