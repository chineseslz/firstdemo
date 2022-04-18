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
from jieKouDemo.mysqlDemo.handle_mysql import HandleDB


@ddt
class TestWithdraw(unittest.TestCase):
    execl = HandleExcel(os.path.join(DATA_DIR, "apicases.xlsx"), 'withdraw')
    cases = execl.read_data()
    db = HandleDB

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

        sql = 'select * from futureloan.member where mobile_phone = "{}" '.format(conf.get("test_data","mobile_phone"))
        # 执行sql前查询余额
        start_amount = self.db.find_one(sql)[0]  #[0]元组数据类型获取

        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()

        # 执行sql后查询余额
        end_amount = self.db.find_one(sql)[0]


        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
            #    校验余额变化
            if res['code'] == 'OK':
                self.assertEqual(float(end_amount-start_amount),params['amount'])
            else:
                #充值失败，余额变化为0
                self.assertEqual(float(end_amount-start_amount),0)
        except AssertionError as e :
            my_log.error("用例---【{}】---执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---【{}】---执行成功".format(item['title']))
