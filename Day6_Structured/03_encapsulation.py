"""
==========================================================================
 Day 6 | Lesson 03 : Encapsulation
==========================================================================
 First principle
   If any line of code anywhere can write account.balance = -5000, then
   no rule about the balance can be trusted. ENCAPSULATION means the
   object guards its own data: outside code asks through methods, and the
   methods check the rules.

 What you will learn
   1. The problem: data anyone can change
   2. One underscore: "internal, please do not touch"
   3. Methods as the only door
   4. Two underscores: Python hides the name
   5. @property: read like an attribute, but cannot be assigned

 Run this file :  python 03_encapsulation.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The problem
# --------------------------------------------------------------------------
class OpenAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc = OpenAccount("Asha", 1000)
acc.balance = -5000                     # no error. The bank is now wrong.
print(acc.balance)                      # -5000

# --------------------------------------------------------------------------
# 2 and 3. Guard the data, give methods as the door
# --------------------------------------------------------------------------
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance         # _ means: internal, use the methods

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be more than zero")
            return
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough balance")
            return
        self._balance = self._balance - amount

    def get_balance(self):
        return self._balance


acc = Account("Asha", 1000)
acc.deposit(500)
acc.withdraw(5000)                      # Not enough balance
print(acc.get_balance())                # 1500
# Every change now passes through a method, so every change is checked.
# The single underscore is a promise between programmers. Python does not
# enforce it: acc._balance = -1 still works, but everyone knows it is wrong.

# --------------------------------------------------------------------------
# 4. Two underscores: a stronger signal
# --------------------------------------------------------------------------
class Locker:
    def __init__(self, pin):
        self.__pin = pin                # __ at the start: Python hides it

    def check(self, guess):
        return guess == self.__pin

locker = Locker(4321)
print(locker.check(1111))               # False
print(locker.check(4321))               # True
# print(locker.__pin)                   # AttributeError: no attribute '__pin'

# --------------------------------------------------------------------------
# 5. @property: looks like an attribute, behaves like a method
# --------------------------------------------------------------------------
class Wallet:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):                   # read with wallet.amount (no brackets)
        return self._amount

    def add(self, value):
        if value > 0:
            self._amount = self._amount + value

wallet = Wallet(200)
wallet.add(50)
print(wallet.amount)                    # 250
# wallet.amount = 999999                # AttributeError: no setter
# Reading is easy, changing must go through add().


# ==========================================================================
# PREDICT before you run!
#
#   acc = Account("Ravi", 300)
#   acc.deposit(-50)
#   acc.withdraw(100)
#   acc.withdraw(500)
#   print(acc.get_balance())
#
# TRY IT YOURSELF
#   1. Add a rule to Account.withdraw: the amount must be more than zero.
#   2. Write a class Student whose marks can be changed only through
#      set_marks(value), and only when value is between 0 and 100.
#   3. Turn Account.get_balance into a @property called balance.
# ==========================================================================
