from bankacct import *
import unittest

class MyTestCases(unittest.TestCase):

    def setUp(self):
        self.bankacct = BankAccount("C01", 1000)

    def test_deposit(self):
        self.assertEqual(self.bankacct.deposit(500), 1500)

    def test_withdraw(self):
        self.assertEqual(self.bankacct.withdraw(300), 700)

    #def test_display(self):
    def tearDown(self):
        self.bankacct = None

    def test_interest(self):
        self.assertEqual(self.bankacct.calc_interest(7),1148)

#__main__
if __name__ == "__main__":
    unittest.main()
