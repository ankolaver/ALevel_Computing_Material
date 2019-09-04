from productvalid import *

import unittest


#testing productval
class MyTestCase(unittest.TestCase):
    def testlength(self):
        self.assertEqual(productval("A37700"),"Code is too short or too long. Within 5 characters")
    def testcapital(self):
        self.assertEqual(productval("b5350"),"First letter should be alphabatical and in CAPS")
    def testnumrange(self):
        self.assertEqual(productval("AB344"),"symbols or letters present")

#main
if __name__ == '__main__':
    unittest.main()
