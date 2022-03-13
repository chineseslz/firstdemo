import unittest
from selenium import webdriver



class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def tearDown(self) -> None:
        self.driver.quit()


    #装饰器：
    def addpic(func):
        def wrapper(self,*args,**kwargs):
            try:
                func(*args,**kwargs)
            except AssertionError as e:
                import os, time
                day = time.strftime('%Y%m%d', time.localtime(time.time()))  # 日期
                screenshot_path = os.getcwd() % day  # 路径
                if not os.path.exists(screenshot_path):
                    os.makedirs(screenshot_path)

                tm = time.strftime("%H%M%S", time.localtime(time.time()))  # 时间
                self.driver.get_screenshot_as_file(screenshot_path + '{}_{}.png'.format('screen_shot', tm))
                raise e  # 将异常继续抛出给unittest
        return wrapper


    @addpic
    def test_demo1(self):
        self.assertEqual(1,2)
