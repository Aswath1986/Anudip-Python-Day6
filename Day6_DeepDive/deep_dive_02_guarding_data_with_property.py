"""
==========================================================================
 Day 6 | Deep Dive 02 : Guarding Data with Properties
==========================================================================
 Goes deeper than Lesson 03.

 First principle
   An object is useful only while its data is valid. Every rule about the
   data ("marks are between 0 and 100") should be written in exactly one
   place, and no assignment should be able to go around it.

 What you will learn
   1. What two underscores really do: name mangling
   2. Private in Python is an agreement, not a lock
   3. @property with a setter: validation on plain assignment
   4. Raising an error instead of printing a message
   5. A computed property: store less, calculate more

 Run this file :  python deep_dive_02_guarding_data_with_property.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Name mangling
# --------------------------------------------------------------------------
class Locker:
    def __init__(self, pin):
        self.__pin = pin

locker = Locker(4321)
print(locker.__dict__)                  # {'_Locker__pin': 4321}
# Python renamed __pin to _Locker__pin. That is why locker.__pin fails
# outside the class: no attribute has that name.

# --------------------------------------------------------------------------
# 2. An agreement, not a lock
# --------------------------------------------------------------------------
print(locker._Locker__pin)              # 4321    it can still be reached
# Python trusts the programmer. The underscores say "this is internal,
# it may change, do not depend on it". Name mangling exists mainly so that
# a child class does not overwrite a parent's attribute by accident.
# In everyday code a single underscore is the usual choice.

# --------------------------------------------------------------------------
# 3. @property with a setter
# --------------------------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks              # goes through the setter below

    @property
    def marks(self):                    # runs on:  student.marks
        return self._marks

    @marks.setter
    def marks(self, value):             # runs on:  student.marks = value
        if not 0 <= value <= 100:
            raise ValueError(f"marks must be 0 to 100, got {value}")
        self._marks = value

asha = Student("Asha", 82)
asha.marks = 90                         # looks like plain assignment
print(asha.marks)                       # 90

# --------------------------------------------------------------------------
# 4. Raise, do not print
# --------------------------------------------------------------------------
try:
    asha.marks = 150
except ValueError as error:
    print("Rejected:", error)           # Rejected: marks must be 0 to 100, got 150
print(asha.marks)                       # 90     the bad value never got in

try:
    Student("Ravi", -5)                 # __init__ uses the same setter
except ValueError as error:
    print("Rejected:", error)
# Lesson 03 printed a message and carried on. A printed message is easy
# to miss, and the caller cannot react to it. An exception (Day 4) stops
# the wrong action and lets the caller decide what to do.

# --------------------------------------------------------------------------
# 5. A computed property
# --------------------------------------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):                     # calculated every time it is read
        return self.length * self.width

r = Rectangle(3, 4)
print(r.area)                           # 12
r.length = 10
print(r.area)                           # 40     always correct
# If area were stored in __init__, it would still say 12 here.
# Rule: do not store what you can calculate from what you already store.


# ==========================================================================
# THINK ABOUT IT
#   1. Inside the setter we write self._marks, not self.marks. What would
#      happen if we wrote  self.marks = value  there?
#   2. Rectangle.area has no setter. What does  r.area = 50  do?
#   3. A getter method (get_balance()) and a property (balance) do the
#      same job. Which reads better at the place where it is used?
#
# PRACTICE
#   Open practice/practice_02_encapsulation.py
# ==========================================================================
