"""
==========================================================================
 Day 6 | Practice 02 : Encapsulation
==========================================================================
 After Lesson 03.   Two TODOs.

 Run :  python practice_02_encapsulation.py
 You are done when every line says PASS.
==========================================================================
"""
from checker import check, summary


class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):          # already written: use it as a model
        if amount > 0:
            self._balance = self._balance + amount

    def withdraw(self, amount):
        # TODO 1: subtract the amount, but only when the amount is not
        #         more than the balance. Otherwise change nothing.
        pass

    def get_balance(self):
        # TODO 2: return the balance.
        pass


def after_withdraw(amount):
    acc = Account(1000)
    acc.withdraw(amount)
    return acc.get_balance()

check("get_balance gives the balance", lambda: Account(1000).get_balance() == 1000)
check("withdrawing 300 leaves 700", lambda: after_withdraw(300) == 700)
check("withdrawing 5000 is refused", lambda: after_withdraw(5000) == 1000)
summary()
