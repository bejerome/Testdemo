__author__ = 'Ben'

import unittest
from Tests.login_test_suite import LoginTest
import os
import HtmlTestRunner

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def testIssue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest),

        ])

        runner1 = HtmlTestRunner.HTMLTestRunner(
            output="./reports/",
            report_title="Demo Test Suite",
            descriptions=True,
            add_timestamp=True,
            open_in_browser=True

        )

        runner1.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
