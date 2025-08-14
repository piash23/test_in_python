import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("John", "Doe", 50000)
        self.emp_2 = Employee("Jane", "Smith", 60000)

    def test_email(self):
        self.assertEqual(self.emp_1.email, "john.doe@company.com")
        self.assertEqual(self.emp_2.email, "jane.smith@company.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "John Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_2.pay, 63000)

    def tearDown(self):
        print("Cleaning up after tests...")


if __name__ == '__main__':
    unittest.main(verbosity=2)