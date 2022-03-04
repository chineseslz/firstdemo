import unittest
from selenium import webdriver

class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print("start---")

    @classmethod
    def tearDownClass(cls):
        print("end---")

    def testFunc1(self):
        print("testFunction1")
        self.assertNotEqual(1,2)

    def testFunc2(self):
        print("testFunction2")
        self.assertEqual(1,2)

if __name__ == '__main__':
    print("diaoyong")
    unittest.main()