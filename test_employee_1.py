
import unittest

# We can import a single class individually
from employee import Employee


class TestEmployee(unittest.TestCase):

    #  https://youtu.be/6tNS--WetLI?t=1335 👈👈

    # setUp: will run this code before every single test
    # 👀 MUST add self.emp_1 for testing to access this setUp
    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 100_000)
        self.emp_2 = Employee('Joseph', 'Yu', 50_000)

    # tearDown: will run this code after every single test
    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'corey.schafer@google.com')
        self.assertEqual(self.emp_2.email, 'joseph.yu@google.com')

        self.emp_1.first = 'Boris'
        self.emp_2.last = 'Johnson'

        self.assertEqual(self.emp_1.email, 'boris.schafer@google.com')
        self.assertEqual(self.emp_2.email, 'joseph.johnson@google.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')

        self.emp_1.first = 'Joseph'
        self.emp_1.last = 'Yu'

        self.assertEqual(self.emp_1.fullname, 'Joseph Yu')

    def test_raise_pay(self):

        self.assertEqual(self.emp_1.pay, 100_000)

        self.emp_1.raise_pay()

        self.assertEqual(self.emp_1.pay, 110_000)


if __name__ == "__main__":
    unittest.main()
