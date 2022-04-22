# -*- coding: utf-8 -*-
# author：slz time:2022/4/21
'''
'''
import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from jieKouDemo.shiZhanDemo.common.handle_excel import HandleExcel
from jieKouDemo.shiZhanDemo.common.handle_path import DATA_DIR
from jieKouDemo.shiZhanDemo.common.handle_conf import conf
from jieKouDemo.mysqlDemo.handle_data import replace_data
from jieKouDemo.shiZhanDemo.common.handler_log import my_log
from jieKouDemo.mysqlDemo.handle_mysql import HandleDB

@ddt
class TestAdd(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'add')
    cases = excel.read_data()
    db = HandleDB

    @classmethod
    def setUpClass(cls) -> None:
        url = conf.get('env', 'base_url') + '/member/login'
        params = {
            'mobile_phone': conf.get('test_data', 'mobile_phone'),
            'pwd': conf.get("test_data", 'pwd')
        }
        headers = eval(conf.get('env', 'headers'))
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()

        token = jsonpath(res, '$..token')[0]
        headers['Authorization'] = 'Beaere' + token
        cls.headers = headers

        cls.member_id = jsonpath(res, "$..id")[0]

    @list_data(cases)
    def test_add(self, item):
        url = conf.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestAdd)
        params = eval(item['data'])
        excepted = eval(item['excepted'])
        method = item['method']

        sql = 'select * from futureloan.loan where member_id = {}'.format(self.member_id)
        start_count = self.db.find_count(sql)

        response = requests.post(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        end_count = self.db.find_count(sql)

        try:
            self.assertEqual(res['code'],excepted['code'])
            self.assertEqual(res['msg'],excepted['msg'])
            if res['msg'] == 'OK':
                self.assertEqual(end_count-start_count,1)
            else:
                self.assertEqual(end_count-start_count,0)

        except AssertionError as e:
            my_log.error("用例---【{}】---执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---【{}】---执行成功".format(item['title']))

