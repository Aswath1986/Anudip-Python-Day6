"""
==========================================================================
 Day 6 | Lesson 06 : Abstraction
==========================================================================
 First principle
   You press a switch and the fan runs. You do not need the wiring.
   You call names.sort() and the list is sorted. You do not need the
   sorting steps. ABSTRACTION means showing WHAT a thing does and hiding
   HOW it does it.
   In a team there is a second problem: Lesson 05 worked only because
   every payment class had a pay method. Nothing forced that. An ABSTRACT
   class is a contract: "every class of this family must provide these
   methods", checked by Python.

 What you will learn
   1. You already use abstraction every day
   2. The problem: a child class that forgot a method
   3. ABC and @abstractmethod: the contract
   4. Python checks the contract for you
   5. Hiding the steps behind one simple method

 Run this file :  python 06_abstraction.py
==========================================================================
"""
from abc import ABC, abstractmethod     # ABC = Abstract Base Class

# --------------------------------------------------------------------------
# 1. You already use it
# --------------------------------------------------------------------------
names = ["Ravi", "Asha", "Meena"]
names.sort()                            # WHAT: sort.  HOW: hidden from you.
print(names)                            # ['Asha', 'Meena', 'Ravi']

# --------------------------------------------------------------------------
# 2. The problem
# --------------------------------------------------------------------------
class LoosePayment:
    pass

class LooseUpi(LoosePayment):
    def pay(self, amount):
        return f"Rs {amount} paid by UPI"

class LooseCard(LoosePayment):
    def pya(self, amount):              # typo: pya. Nobody notices today.
        return f"Rs {amount} paid by card"

card = LooseCard()                      # no error here
# card.pay(200)                         # AttributeError, but only when a
#                                       # customer finally pays by card.

# --------------------------------------------------------------------------
# 3. The contract
# --------------------------------------------------------------------------
class Payment(ABC):                     # an abstract class
    def __init__(self, customer):
        self.customer = customer

    @abstractmethod
    def pay(self, amount):              # WHAT every payment must do.
        pass                            # No HOW here.

    def receipt(self, amount):          # ordinary methods are allowed too
        return f"{self.customer}: {self.pay(amount)}"


class Upi(Payment):
    def pay(self, amount):              # the HOW, for UPI
        return f"Rs {amount} paid by UPI"

class Card(Payment):
    def pay(self, amount):              # the HOW, for card
        return f"Rs {amount + amount * 2 / 100} paid by card"


for payment in [Upi("Asha"), Card("Ravi")]:
    print(payment.receipt(200))
# Asha: Rs 200 paid by UPI
# Ravi: Rs 204.0 paid by card

# --------------------------------------------------------------------------
# 4. Python checks the contract
# --------------------------------------------------------------------------
# An abstract class is an idea, not a thing. You cannot make one:
# p = Payment("Asha")                   # TypeError: Can't instantiate
#                                       # abstract class Payment ...

class BrokenCash(Payment):
    def pya(self, amount):              # the same typo as before
        return f"Rs {amount} paid in cash"

try:
    cash = BrokenCash("Meena")
except TypeError as error:
    print("Caught:", error)
# The mistake is caught the moment the object is made, not weeks later
# at the billing counter.

# --------------------------------------------------------------------------
# 5. Hiding the steps
# --------------------------------------------------------------------------
class TeaMachine:
    def make_tea(self):                 # the one button the user sees
        self._boil_water()
        self._add_tea_leaves()
        self._add_milk_and_sugar()
        return "Tea is ready"

    def _boil_water(self):              # internal steps (Lesson 03: _)
        print("  boiling water")

    def _add_tea_leaves(self):
        print("  adding tea leaves")

    def _add_milk_and_sugar(self):
        print("  adding milk and sugar")

print(TeaMachine().make_tea())
# Encapsulation protects the DATA. Abstraction hides the STEPS.
# They are used together: a small public face, everything else inside.


# ==========================================================================
# PREDICT before you run!
#
#   class Shape(ABC):
#       @abstractmethod
#       def area(self):
#           pass
#
#   class Square(Shape):
#       def __init__(self, side):
#           self.side = side
#       def area(self):
#           return self.side ** 2
#
#   class Blob(Shape):
#       pass
#
#   print(Square(3).area())
#   b = Blob()              # what happens on this line?
#
# TRY IT YOURSELF
#   1. Add a class Cash(Payment) with a correct pay method. Print its
#      receipt.
#   2. Write an abstract class Notifier with an abstract method
#      send(message). Write SmsNotifier and EmailNotifier.
#   3. Add a second abstract method refund(amount) to Payment. Run the
#      file. Which classes break, and where does Python tell you?
# ==========================================================================
