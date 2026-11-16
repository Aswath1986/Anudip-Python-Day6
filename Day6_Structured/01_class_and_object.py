"""
==========================================================================
 Day 6 | Lesson 01 : Class and Object
==========================================================================
 First principle
   A student has data (name, marks) and rules (has the student passed?).
   With a dict and loose functions, nothing ties the two together, every
   dict is typed by hand, and one spelling mistake in a key breaks it.
   A CLASS is a blueprint that keeps the data and its rules in one place.
   An OBJECT is one real thing built from that blueprint.

 What you will learn
   1. The problem with dicts and loose functions
   2. class, __init__ and self
   3. Making objects and reading their attributes
   4. Methods: functions that live inside the class
   5. Each object keeps its own data

 Run this file :  python 01_class_and_object.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The problem
# --------------------------------------------------------------------------
asha = {"name": "Asha", "marks": 82}
ravi = {"name": "Ravi", "mark": 67}     # typo: "mark". Python does not complain.

def has_passed(student):
    return student["marks"] >= 40

print(has_passed(asha))                 # True
# print(has_passed(ravi))               # KeyError: 'marks'
# The mistake was made when ravi was created, but the error appears much
# later, somewhere else. We want one place that decides what a student has.

# --------------------------------------------------------------------------
# 2. The blueprint
# --------------------------------------------------------------------------
class Student:
    def __init__(self, name, marks):    # runs once, when an object is made
        self.name = name                # self = the object being built
        self.marks = marks

    def has_passed(self):               # a METHOD: a function inside a class
        return self.marks >= 40

    def add_grace(self, extra):
        self.marks = self.marks + extra

# --------------------------------------------------------------------------
# 3. Making objects
# --------------------------------------------------------------------------
asha = Student("Asha", 82)              # calls __init__(asha, "Asha", 82)
ravi = Student("Ravi", 35)

print(asha.name)                        # Asha     (an ATTRIBUTE: object.name)
print(ravi.marks)                       # 35
print(type(asha))                       # <class '__main__.Student'>

# Forget a value and Python tells you at once, at the right line:
# meena = Student("Meena")              # TypeError: missing ... 'marks'

# --------------------------------------------------------------------------
# 4. Calling methods
# --------------------------------------------------------------------------
print(asha.has_passed())                # True
print(ravi.has_passed())                # False
# You write asha.has_passed(). Python passes asha in as self for you.

# --------------------------------------------------------------------------
# 5. Each object keeps its own data
# --------------------------------------------------------------------------
ravi.add_grace(5)
print(ravi.marks)                       # 40
print(ravi.has_passed())                # True
print(asha.marks)                       # 82   (asha did not change)

# One blueprint, many objects. You have used this since Day 1:
# "hello".upper()  ->  "hello" is an object of class str, upper is a method.


# ==========================================================================
# PREDICT before you run!
#
#   class Dog:
#       def __init__(self, name):
#           self.name = name
#       def speak(self):
#           return self.name + " says woof"
#
#   a = Dog("Tommy")
#   b = Dog("Rocky")
#   print(a.speak())
#   print(b.name)
#   print(a is b)
#
# TRY IT YOURSELF
#   1. Add a method grade() to Student: "A" for 75 and above, "B" for 40
#      and above, otherwise "F". Call it on asha and ravi.
#   2. Write a class Book with title and price, and a method
#      price_with_gst() that returns the price plus 5 percent.
#   3. Make three Book objects, put them in a list, and print each title
#      with a for loop.
# ==========================================================================
