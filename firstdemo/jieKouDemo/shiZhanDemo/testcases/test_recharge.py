# -*- coding: utf-8 -*-
# author：slz time:2022/4/2
'''
'''
import unittest
import os
from unittestreport import ddt,list_data
from ..common.handle_excel import HandleExcel
from ..common.handle_path import DATA_DIR

@ddt
class TestRecharge(unittest.TestCase):
    execl = HandleExcel(os.path.join(DATA_DIR,"apicases.xlsx"),'recharge')
    cases = execl.read_data()

    @classmethod
    def setUpClass(cls):
        """"""

    @list_data(cases)
    def test_recharge(self,item):
        pass
