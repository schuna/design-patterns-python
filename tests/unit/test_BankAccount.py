import contextlib
import io
from unittest import TestCase

from design_patterns.command.BankAccount import BankAccount, BankAccountCommand, CompositeBankAccountCommand, \
    MoneyTransferCommand


class TestBankAccountCommand(TestCase):
    def setUp(self) -> None:
        self.bank_account = BankAccount()
        self.bank_account2 = BankAccount()
        self.command = BankAccountCommand(
            self.bank_account,
            BankAccountCommand.Action.DEPOSIT,
            100)
        self.command2 = BankAccountCommand(
            self.bank_account2,
            BankAccountCommand.Action.DEPOSIT,
            1000
        )

    def test_deposit_successful(self):
        expected = "Deposited 100, balance = 100\n"
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.command.invoke()
        self.assertEqual(expected, buf.getvalue())

    def test_withdraw_successful(self):
        expected = "Withdrew 100, balance = 0\n"
        self.command.invoke()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.command.undo()
        self.assertEqual(expected, buf.getvalue())

    def test_withdraw_illegal(self):
        command = BankAccountCommand(
            self.bank_account,
            BankAccountCommand.Action.WITHDRAW,
            1000)
        command.invoke()
        self.assertEqual(0, self.bank_account.balance)
        command.undo()
        self.assertEqual(0, self.bank_account.balance)

    def test_composite_bank_account_successful(self):
        composite = CompositeBankAccountCommand([self.command, self.command])
        composite.invoke()
        self.assertEqual(200, self.bank_account.balance)
        composite.undo()
        self.assertEqual(0, self.bank_account.balance)

    def test_money_transfer_command_successful(self):
        self.command.invoke()
        self.command2.invoke()
        transfer = MoneyTransferCommand(self.bank_account2, self.bank_account, 500)
        transfer.invoke()
        self.assertEqual(500, self.bank_account2.balance)
        self.assertEqual(600, self.bank_account.balance)
