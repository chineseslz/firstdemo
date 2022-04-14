# -*- coding: utf-8 -*-
# author：slz time:2022/4/1
'''
'''
import unittest
import os
import requests
import random
from unittestreport import ddt, list_data
from ..common.handle_excel import HandleExcel
from ..common.handle_path import DATA_DIR
from ..common.handle_conf import conf
from ..common.handler_log import my_log


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'register')
    # 读取用例数据
    cases = excel.read_data()
    base_url = conf.get("env", "base_url")
    headers = eval(conf.get("env", "headers"))

    @list_data(cases)
    def test_register(self, item):
        # 第一步，准备用例数据
        # 1.接口地址
        url = self.base_url + item['url']
        # 2.请求参数
        if '#mobile' in item['data']:
            phone = self.random_mobile()
            item['data'] = item['data'].replace('#mobile#',phone)
        #excel读取出字符串转换一下
        params = eval(item["data"])
        # 3.请求头
        # 4.请求方法
        method = item["method"].lower()
        # 5.预期结果
        expected = item["expected"]

        # 第二步：请求接口，获取返回实际结果
        response = requests.request(method=method,url=url,json=params,headers=self.headers)
        res = response.json()

        # 第三步：断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e :
            #记录日志
            my_log.error("用例---【{}】---执行失败".format(item['title']))
            my_log.error(e)
            raise e
        else:
            my_log.info("用例---【{}】---执行通过".format(item['title']))

    def random_mobile(self):
        '''随机生产手机号'''
        phone = str(random.randint(13300000000,13399999999))
        return phone