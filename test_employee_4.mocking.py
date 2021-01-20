# Jan 20 2020

"""
😎 The setUp and tearDown 

    1. setUp & tearDown will perform for every single test
    2. testing sequence DO NOT necessarily run in the order you expect! 测试的顺序并非脚本顺序！
    3. keep ALL of our test isolated from eachother 每个功能的测试必须独立，分治，自洽

# 👀 cls和self之间只能二选一！不能同时继承！
# recall: @classmethod -> working with the ENTIRE class rather than each instance of the class

# 🎯 mocking: https://youtu.be/6tNS--WetLI?t=1720 ⏭
"""

import requests
import unittest
from employee import Employee
from unittest.mock import patch


###### With Prints ######


class TestEmployee(unittest.TestCase):
    """ Run classmethod before ANYTYING & run after EVERYTYING """
    @classmethod
    def setUpClass(cls):
        print('Run setupClass!')
        print()

    @classmethod
    def tearDownClass(cls):
        print('Run teardownClass!')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50_000)
        self.emp_2 = Employee('Sue', 'Smith', 60_000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@google.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@google.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@google.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@google.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_raise_pay(self):
        print('test_raise_pay')
        self.emp_1.raise_pay()
        self.emp_2.raise_pay()

        self.assertEqual(self.emp_1.pay, 55000)
        self.assertEqual(self.emp_2.pay, 66000)

    ##### Mocking #####

    def test_monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


if __name__ == '__main__':
    unittest.main()


###### setUpClass and tearDownClass ######
