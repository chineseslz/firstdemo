import unittest

class numberTests(unittest.TestCase):

    def testNum1(self):
        self.assertIn("hello","hello world")

    def testNum2(self):
        self.assertNotIn("hello","hello world")