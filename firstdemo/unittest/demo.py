import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class demo(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) :
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get("https://www.baidu.com/")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("end---")

    def setUp(self) -> None:
        print("---start---")
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        time.sleep(1)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
        print("---end---")

    def test_login_success(self):
        '''
        正确用户名/密码，登陆成功
        :return:
        '''
        self.driver.get(self.url)
        self.driver.find_element("id","s-top-loginbtn").click()
        time.sleep(1)
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__userName"]').send_keys("admin")
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__password"]').send_keys("admin")
        login_submit = self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__password"]')
        print(login_submit)
        login_name = self.driver.find_element("id",'login_name').text
        self.assertEqual("admin",login_name)

    def test_login_failed_without_username(self):
        '''
        用户名为空，登录失败
        :return:
        '''
        self.driver.get(self.url)
        self.driver.find_element("id","s-top-loginbtn").click()
        time.sleep(1)
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__password"]').send_keys("admin")
        login_submit = self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__password"]')
        login_submit.click()
        errmsg = self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__error"]').text
        self.assertEqual(errmsg,"请您输入手机号/用户名/邮箱")

if __name__ == '__main__':
    print("---main调用---")
    unittest.main()