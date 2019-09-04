from agevalid import *
import unittest

class MyTestCases(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(age_valid(''),"Empty input")

    #call up main class first followed by testing
    def test_digit(self):
        self.assertEqual(age_valid("Joe"),"Age must be a number")

    def test_realage(self):
        self.assertEqual(age_valid(111),"Age must be between 1 and 109")


#__main__
if __name__ == "__main__":
    unittest.main()
