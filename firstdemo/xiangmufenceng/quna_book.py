'''
    业务逻辑层代码
'''
from selenium.webdriver.common.action_chains import ActionChains
from base_function import *
import time
from selenium.webdriver.common.keys import Keys

def book_ticket(start,end,n,name,id):
    '''
    :param start: 出发地
    :param end: 目的地
    :param n: 天数（）
    :param name: 姓名
    :param id: 身份证
    :return:
    '''
