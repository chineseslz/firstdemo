import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
    def tearDown(self) -> None:
        self.driver.quit()

    def find_element(self,locator):
        try:
            element = WebDriverWait(self.driver,30,0.5).until(lambda x: x.find_element(*locator))
            return element
        except NoSuchElementException as e :
            print('Error details:{}'.format(e.args[0]))

    def test1(self):
        time.sleep(1)
        self.driver.find_element("id", "s-top-loginbtn").click()
        time.sleep(2)
        self.find_element("xpath", '//*[@id="TANGRAM__PSP_11__userName"]').send_keys("admin")
        self.find_element("xpath", '//*[@id="TANGRAM__PSP_11__password"]').send_keys("admin")
        self.find_element("xpath", '//*[@id="TANGRAM__PSP_11__submit"]').click()
        self.find_element(('partial link text','个人中心')).click()