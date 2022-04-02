import unittest
from ..shiZhanDemo.common.handle_path import CASES_DIR, REPORT_DIR
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(CASES_DIR)

runner = TestRunner(suite,
                    filename="jiekouDemo.html",
                    report_dir=REPORT_DIR,
                    )

runner.run()
