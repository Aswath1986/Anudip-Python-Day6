"""
==========================================================================
 Day 6 | Lesson 02 : Attributes and Methods
==========================================================================
 First principle
   Some facts belong to one student (a name). Some facts belong to every
   student (the pass mark, the centre name). Storing a shared fact inside
   every object repeats it, and changing it means changing every object.
   An INSTANCE attribute belongs to one object. A CLASS attribute is
   written once and shared by all of them.

 What you will learn
   1. Instance attributes and class attributes
   2. Changing a shared value in one place
   3. __str__: what print() shows for your object
   4. A method that uses another method

 Run this file :  python 02_attributes_and_methods.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Two kinds of attribute
# --------------------------------------------------------------------------
class Student:
    centre = "Anudip Chennai"           # CLASS attribute: one copy, shared
    pass_mark = 40

    def __init__(self, name, marks):
        self.name = name                # INSTANCE attributes: one per object
        self.marks = marks

    def has_passed(self):
        return self.marks >= Student.pass_mark

    def result(self):                   # a method may call another method
        if self.has_passed():
            return "PASS"
        return "FAIL"

    def __str__(self):                  # used by print() and str()
        return f"{self.name} ({self.marks}) {self.result()}"


asha = Student("Asha", 82)
ravi = Student("Ravi", 38)

print(asha.name, "|", ravi.name)        # Asha | Ravi        (different)
print(asha.centre, "|", ravi.centre)    # Anudip Chennai | Anudip Chennai

# --------------------------------------------------------------------------
# 2. Change the shared value once
# --------------------------------------------------------------------------
print(ravi.result())                    # FAIL
Student.pass_mark = 35                  # one change, on the class
print(ravi.result())                    # PASS
print(asha.result())                    # PASS

# --------------------------------------------------------------------------
# 3. __str__
# --------------------------------------------------------------------------
print(asha)                             # Asha (82) PASS
# Without __str__ you would see something like
# <__main__.Student object at 0x7f...>, which helps nobody.

# Names with two underscores on each side (__init__, __str__) are methods
# that Python calls for you at a fixed moment. You do not call them by name.

# --------------------------------------------------------------------------
# 4. Objects in a list, with yesterday's tools
# --------------------------------------------------------------------------
batch = [asha, ravi, Student("Meena", 91), Student("Bo", 20)]

for student in batch:
    print(student)

topper = max(batch, key=lambda s: s.marks)
print("Topper:", topper.name)           # Topper: Meena

passed = list(filter(lambda s: s.has_passed(), batch))
print(len(passed))                      # 3


# ==========================================================================
# PREDICT before you run!
#
#   class Counter:
#       step = 1
#       def __init__(self):
#           self.value = 0
#       def tick(self):
#           self.value = self.value + Counter.step
#
#   a = Counter()
#   b = Counter()
#   a.tick()
#   a.tick()
#   Counter.step = 10
#   b.tick()
#   print(a.value, b.value)
#
# TRY IT YOURSELF
#   1. Add a class attribute course = "Python" and show it in __str__.
#   2. Write a class Product with name and price, a class attribute
#      gst_rate = 5, and a method final_price().
#   3. Give Product a __str__ so that print(product) shows
#      "Pen: Rs 10.5".
# ==========================================================================
