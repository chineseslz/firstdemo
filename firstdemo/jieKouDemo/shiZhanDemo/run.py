import unittest

from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'C:\testproject\firstdemo\firstdemo\firstdemo\jieKouDemo\shiZhanDemo\testcases')

runner = TestRunner(suite,
                    filename="",
                    report_dir=r"C:\testproject\firstdemo\firstdemo\firstdemo\jieKouDemo\shiZhanDemo\logs",
                    )

runner.run()
