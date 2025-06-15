import unittest
from TsheringChophey_02240104_A3 import BankAccount, PersonalAccount, BusinessAccount, InvalidTransactionError, InvalidTransferError, BankingSystem

class TestBankingFunctions(unittest.TestCase):

    def setUp(self):
        self.account1 = PersonalAccount("12345", "1111", 1000)
        self.account2 = BusinessAccount("54321", "2222", 500)

    def test_deposit_valid(self):
        result = self.account1.deposit(200)
        self.assertEqual(self.account1.funds, 1200)
        self.assertEqual(result, "Deposit completed.")

    def test_deposit_invalid(self):
        with self.assertRaises(InvalidTransactionError):
            self.account1.deposit(-50)

    def test_withdraw_valid(self):
        result = self.account1.withdraw(300)
        self.assertEqual(self.account1.funds, 700)
        self.assertEqual(result, "Withdrawal completed.")

    def test_withdraw_invalid(self):
        with self.assertRaises(InvalidTransactionError):
            self.account1.withdraw(2000)

    def test_transfer_valid(self):
        result = self.account1.transfer(400, self.account2)
        self.assertEqual(result, "Transfer completed.")
        self.assertEqual(self.account1.funds, 600)
        self.assertEqual(self.account2.funds, 900)

    def test_transfer_invalid(self):
        with self.assertRaises(InvalidTransferError):
            self.account1.transfer(2000, self.account2)

    def test_top_up_mobile_valid(self):
        result = self.account1.top_up_mobile("17451234", 100)
        self.assertEqual(self.account1.funds, 900)
        self.assertEqual(result, "Topped up Nu. 100 to 17451234.")

    def test_top_up_mobile_invalid_number(self):
        with self.assertRaises(InvalidTransactionError):
            self.account1.top_up_mobile("123", 50)

    def test_top_up_mobile_insufficient_funds(self):
        with self.assertRaises(InvalidTransactionError):
            self.account1.top_up_mobile("17451234", 2000)

    def test_account_login_success(self):
        bank = BankingSystem(filename="test_accounts.txt")
        acc = PersonalAccount("99999", "4321", 300)
        bank.accounts["99999"] = acc
        result = bank.login("99999", "4321")
        self.assertEqual(result, acc)

    def test_account_login_failure(self):
        bank = BankingSystem(filename="test_accounts.txt")
        with self.assertRaises(ValueError):
            bank.login("00000", "9999")

    def test_account_deletion(self):
        bank = BankingSystem(filename="test_accounts.txt")
        acc = PersonalAccount("12345", "0000", 300)
        bank.accounts["12345"] = acc
        bank.delete_account("12345")
        self.assertNotIn("12345", bank.accounts)

if __name__ == '__main__':
    unittest.main()
