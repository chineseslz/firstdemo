import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from HTMLTestRunner import HTMLTestReportCN


class loginTest(unittest.TestCase):

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
        self.imgs = []
        self.driver.maximize_window()
        self.url = "https://www.baidu.com/"
        time.sleep(1)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
        print("---end---")

    def test_login_success(self):
        '''
        错误用户名/密码，登陆失败
        :return:
        '''
        self.driver.get(self.url)
        self.driver.find_element("id","s-top-loginbtn").click()
        time.sleep(2)
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__userName"]').send_keys("admin")
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__password"]').send_keys("admin")
        self.driver.find_element("xpath",'//*[@id="TANGRAM__PSP_11__submit"]').click()
        time.sleep(1)
        self.imgs.append(self.driver.get_screenshot_as_base64())
        errmsg = self.driver.find_element("xpath",'//*[text()="用户名或密码有误，请重新输入或"]').text
        print(errmsg)
        self.assertEqual("用户名或密码有误，请重新输入或",errmsg)

if __name__ == '__main__':
    test1 = unittest.defaultTestLoader.loadTestsFromTestCase(loginTest)
    suite = unittest.TestSuite(test1)

    runner = HTMLTestReportCN(
        title = '带截图的测试报告',
        description="xxx测试报告V1.0",
        stream=open('est_report.html','wb'),
        verbosity=2
    )