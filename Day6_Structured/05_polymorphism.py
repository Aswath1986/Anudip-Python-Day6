"""
==========================================================================
 Day 6 | Lesson 05 : Polymorphism
==========================================================================
 First principle
   The canteen accepts UPI, card and cash. If the billing code says
   "if UPI do this, elif card do that, elif cash ...", then every new way
   to pay means opening and editing the billing code again.
   POLYMORPHISM means many kinds of object answer the SAME method name,
   each in its own way. The caller writes one line and never asks which
   kind it is holding.

 What you will learn
   1. You already use it: len() and +
   2. The problem: an if / elif chain on type
   3. Same method name, different classes
   4. Polymorphism through inheritance
   5. Your own class can answer len() and +

 Run this file :  python 05_polymorphism.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. You already use it
# --------------------------------------------------------------------------
print(len("Asha"))                      # 4    characters
print(len([10, 20, 30]))                # 3    items
print(len({"a": 1}))                    # 1    keys
print(2 + 3, "2" + "3")                 # 5 23   one symbol, two behaviours

# --------------------------------------------------------------------------
# 2. The problem
# --------------------------------------------------------------------------
def pay_old(kind, amount):
    if kind == "upi":
        return f"Rs {amount} paid by UPI"
    elif kind == "card":
        return f"Rs {amount + amount * 2 / 100} paid by card (2% fee)"
    elif kind == "cash":
        return f"Rs {amount} paid in cash"
    # a new way to pay = edit this function again

print(pay_old("card", 200))             # Rs 204.0 paid by card (2% fee)

# --------------------------------------------------------------------------
# 3. Same method name, each class in its own way
# --------------------------------------------------------------------------
class Upi:
    def pay(self, amount):
        return f"Rs {amount} paid by UPI"

class Card:
    def pay(self, amount):
        return f"Rs {amount + amount * 2 / 100} paid by card (2% fee)"

class Cash:
    def pay(self, amount):
        return f"Rs {amount} paid in cash"


def checkout(method, amount):
    print(method.pay(amount))           # one line. No if, no type check.

for method in [Upi(), Card(), Cash()]:
    checkout(method, 200)

# A new way to pay is a new class. checkout() is not touched:
class Wallet:
    def pay(self, amount):
        return f"Rs {amount} paid from wallet"

checkout(Wallet(), 200)                 # Rs 200 paid from wallet
# Python asks only one question: does this object have a pay method?
# This is called duck typing: if it walks like a duck, treat it as a duck.

# --------------------------------------------------------------------------
# 4. Polymorphism through inheritance
# --------------------------------------------------------------------------
class Shape:
    def area(self):
        return 0

    def describe(self):                 # written once, in the parent
        return f"{type(self).__name__} with area {self.area()}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

for shape in [Square(4), Rectangle(3, 5)]:
    print(shape.describe())
# Square with area 16
# Rectangle with area 15
# describe() calls self.area(), and self decides which area() runs.

# --------------------------------------------------------------------------
# 5. Your class can answer len() and +
# --------------------------------------------------------------------------
class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):                  # len(cart) calls this
        return len(self.items)

    def __add__(self, other):           # cart + cart calls this
        return Cart(self.items + other.items)

morning = Cart(["tea", "idli"])
evening = Cart(["coffee"])
print(len(morning))                     # 2
print(len(morning + evening))           # 3


# ==========================================================================
# PREDICT before you run!
#
#   class Dog:
#       def speak(self):
#           return "Woof"
#
#   class Cat:
#       def speak(self):
#           return "Meow"
#
#   class Robot:
#       def speak(self):
#           return "Beep"
#
#   for thing in [Dog(), Robot(), Cat()]:
#       print(thing.speak())
#
# TRY IT YOURSELF
#   1. Add a class NetBanking with a pay method and send it to checkout().
#      Did you change checkout()?
#   2. Add a class Circle(Shape) with a radius. Use 3.14 * radius * radius.
#   3. Give Cart a __str__ so that print(morning) shows "Cart: tea, idli".
#      Hint: ", ".join(self.items)
# ==========================================================================
