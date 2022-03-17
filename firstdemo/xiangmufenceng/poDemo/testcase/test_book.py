'''
    测试代码
'''
import pytest

from firstdemo.xiangmufenceng.poDemo.po.book_ticket_page import Bookticket
from selenium import webdriver
from firstdemo.xiangmufenceng.poDemo.common.function import *


data = read_excel("aaa.txt", 0, True)

class Test_book():
    def setup(self):
        self.driver = webdriver.chrome()
        self.driver.get("")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(["start","end","n","name","id"],data)
    def test_01(self,start,end,n,name,id):
        ticket = Bookticket(self.driver)
        ticket.book_ticket(start,end,date_n(n))
