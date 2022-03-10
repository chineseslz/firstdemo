import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack

@ddt
class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.data = [
            ('','pwd','用户名 不能为空'),
            ('admin', '', '密码 不能为空'),
            ('adminx', 'pwd123', '没有此用户'),
            ('admin', 'pwd123', '密码错误')
        ]

    def tearDown(self) -> None:
        self.driver.quit()

    @data(1,2,3,4)
    def test_data(self,value):
        print(value)   #打印1，2，3，4

    @unpack
    def test_login_filed(self,username,password,err):


    def test_login(self):
        '''
        多数据测试
        :return:
        '''
        time.sleep(2)
        self.driver.find_element("id", "s-top-loginbtn").click()
        time.sleep(2)
        for data in self.data:
            self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__userName"]').clear()
            self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__userName"]').send_keys(data[0])
            self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__password"]').clear()
            self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__password"]').send_keys(data[1])
            self.driver.find_element("xpath", '//*[@id="TANGRAM__PSP_11__submit"]').click()
            errmsg = self.driver.find_element('xpath','//*[text()="{}"]'.format(data[2])).text
            self.assertEqual(errmsg,data[2])