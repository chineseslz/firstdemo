import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack
from util import util

@ddt
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')


    def tearDown(self) -> None:
        self.driver.quit()

    # #参数
    # @data(
    #     ('', 'pwd', '用户名 不能为空'),
    #     ('admin', '', '密码 不能为空'),
    #     ('adminx', 'pwd123', '没有此用户'),
    #     ('admin', 'pwd123', '密码错误')
    # )

    # #参数
    # @data(*util.get_data())
    @data(*util.get_data_from_file('data.txt'))
    #包装参数
    @unpack
    def test_login_filed(self,username,password,err):
        '''
        多数据测试
        :return:
        '''
        time.sleep(2)
        self.driver.find_element("id", "s-top-loginbtn").click()
        time.sleep(2)
        self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__userName"]').clear()
        self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__userName"]').send_keys(username)
        self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__password"]').clear()
        self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__password"]').send_keys(password)
        self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__submit"]').click()
        errmsg = self.driver.find_element('xpath','//*[text()="{}"]'.format(err)).text
        self.assertEqual(errmsg,err)