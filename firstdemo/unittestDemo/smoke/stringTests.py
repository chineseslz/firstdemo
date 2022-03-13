import unittest

class stringTests(unittest.TestCase):

    def testStr1(self):
        self.assertIn("hello","hello world")

    def testStr2(self):
        self.assertNotIn("hello","hello world")