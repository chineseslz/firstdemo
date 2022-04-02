# -*- coding: utf-8 -*-
# author：slz time:2022/4/2
'''
同一个接口不同用例返回的字段不一样如何处理.py
'''
import unittest


class TestDemo(unittest.TestCase):

    def test_demo(self):
        # 实际结果
        res = {"code": 0, "msg": "OK", "time": '20201212'}
        # 预期结果
        exceptd = {"code": 0, "msg": "OK", }

        # self.assertEqual(exceptd['code'], res['code'])
        # self.assertEqual(exceptd['msg'], res['msg'])

        self.assertDictIn(exceptd, res)

    def assertDictIn(self, exceptd, res):
        for k, v in exceptd.items():
            if res.get(k) == v:
                print(res.get(k))
            else:
                raise AssertionError("{} not in {}".format(exceptd, res))
