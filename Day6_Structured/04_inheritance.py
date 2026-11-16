"""
==========================================================================
 Day 6 | Lesson 04 : Inheritance
==========================================================================
 First principle
   A student has a name and a city. A trainer has a name and a city.
   Writing the same __init__ and the same methods in both classes is
   copy-paste, and a bug has to be fixed in two places.
   INHERITANCE lets a new class start with everything an existing class
   has, then add or change only what is different.

 What you will learn
   1. The problem: two classes with repeated code
   2. A parent class and child classes
   3. super(): let the parent do its part
   4. Overriding: the child replaces a method
   5. isinstance(): a Student IS A Person

 Run this file :  python 04_inheritance.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The problem (do not write this)
# --------------------------------------------------------------------------
# class Student:                         class Trainer:
#     def __init__(self, name, city):        def __init__(self, name, city):
#         self.name = name                       self.name = name
#         self.city = city                       self.city = city
#     def intro(self): ...                   def intro(self): ...
# The same lines twice. Add "phone" and you must edit both.

# --------------------------------------------------------------------------
# 2. The parent: what every person has
# --------------------------------------------------------------------------
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def intro(self):
        return f"I am {self.name} from {self.city}"

# --------------------------------------------------------------------------
# 3. Children: only what is different
# --------------------------------------------------------------------------
class Student(Person):                  # Student inherits from Person
    def __init__(self, name, city, marks):
        super().__init__(name, city)    # the parent sets name and city
        self.marks = marks              # the child adds marks

    def has_passed(self):               # a new method, only for students
        return self.marks >= 40


class Trainer(Person):
    def __init__(self, name, city, subject):
        super().__init__(name, city)
        self.subject = subject

    def intro(self):                    # OVERRIDE: same name, new behaviour
        return f"I am {self.name}, I teach {self.subject}"


asha = Student("Asha", "Chennai", 82)
kumar = Trainer("Kumar", "Madurai", "Python")

print(asha.intro())                     # I am Asha from Chennai   (inherited)
print(asha.has_passed())                # True                     (its own)
print(kumar.intro())                    # I am Kumar, I teach Python (overridden)
print(kumar.city)                       # Madurai                  (inherited)

# --------------------------------------------------------------------------
# 4. Extend instead of replace
# --------------------------------------------------------------------------
class Mentor(Trainer):                  # a child of a child
    def intro(self):
        return super().intro() + " and I mentor new trainers"

print(Mentor("Latha", "Salem", "SQL").intro())
# I am Latha, I teach SQL and I mentor new trainers

# --------------------------------------------------------------------------
# 5. The IS A test
# --------------------------------------------------------------------------
print(isinstance(asha, Student))        # True
print(isinstance(asha, Person))         # True    a Student is a Person
print(isinstance(asha, Trainer))        # False
# Use inheritance only when "child IS A parent" sounds true.
# A Student is a Person: yes. A Classroom is a Student: no.


# ==========================================================================
# PREDICT before you run!
#
#   class Animal:
#       def __init__(self, name):
#           self.name = name
#       def sound(self):
#           return "..."
#
#   class Cat(Animal):
#       def sound(self):
#           return "Meow"
#
#   class Cow(Animal):
#       pass
#
#   print(Cat("Kitty").sound())
#   print(Cow("Lakshmi").sound())
#   print(Cow("Lakshmi").name)
#
# TRY IT YOURSELF
#   1. Add a phone attribute to Person. How many classes did you edit?
#   2. Write class Vehicle with brand and wheels, and a method describe().
#      Write Bike(Vehicle) and Car(Vehicle) that set wheels to 2 and 4
#      using super().__init__.
#   3. Override describe() in Car so that it also says "with AC".
# ==========================================================================
