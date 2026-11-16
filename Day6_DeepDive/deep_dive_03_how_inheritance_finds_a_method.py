"""
==========================================================================
 Day 6 | Deep Dive 03 : How Inheritance Finds a Method
==========================================================================
 Goes deeper than Lesson 04.

 First principle
   Deep Dive 01: Python looks for a name in the object, then in its class.
   Inheritance adds one more step to the same search: then in the parent,
   then in the parent's parent, and so on. Nothing is copied into the
   child. Inheritance is a search path.

 What you will learn
   1. The search path of a class: __mro__
   2. Every class ends at object
   3. What super() does, and what happens if you forget it
   4. Two parents: the order of the search
   5. HAS A: when inheritance is the wrong tool

 Run this file :  python deep_dive_03_how_inheritance_finds_a_method.py
==========================================================================
"""

class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"I am {self.name}"

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

# --------------------------------------------------------------------------
# 1. The search path
# --------------------------------------------------------------------------
print([c.__name__ for c in Student.__mro__])    # ['Student', 'Person', 'object']
# MRO = Method Resolution Order. For asha.intro() Python checks Student
# (not there), then Person (found, stop).

asha = Student("Asha", 82)
print("intro" in Student.__dict__)      # False   nothing was copied
print(asha.intro())                     # I am Asha

# --------------------------------------------------------------------------
# 2. Everything ends at object
# --------------------------------------------------------------------------
class Empty:
    pass

print(Empty.__mro__[-1])                # <class 'object'>
print(Empty())                          # <__main__.Empty object at 0x...>
# Empty has no __str__, yet print works. It was found in object.
# When you write __str__ you are overriding the one in object.

# --------------------------------------------------------------------------
# 3. Forgetting super()
# --------------------------------------------------------------------------
class Trainer(Person):
    def __init__(self, name, subject):
        self.subject = subject          # forgot super().__init__(name)

kumar = Trainer("Kumar", "Python")
try:
    print(kumar.intro())
except AttributeError as error:
    print("Error:", error)              # ... object has no attribute 'name'
# The child's __init__ REPLACED the parent's, so name was never set.
# super().__init__(name) means "run the next __init__ on the search path".

# --------------------------------------------------------------------------
# 4. Two parents
# --------------------------------------------------------------------------
class Singer:
    def perform(self):
        return "sings"

class Dancer:
    def perform(self):
        return "dances"

class Artist(Singer, Dancer):           # the order written here matters
    pass

print(Artist().perform())               # sings
print([c.__name__ for c in Artist.__mro__])
# ['Artist', 'Singer', 'Dancer', 'object']   left to right
# Two parents are allowed but rarely needed. When both have the same
# method, the reader must know the MRO to know what runs.

# --------------------------------------------------------------------------
# 5. HAS A instead of IS A
# --------------------------------------------------------------------------
# Wrong: class Classroom(Student). A classroom is not a student.
# A classroom HAS students. Put objects inside an object:
class Classroom:
    def __init__(self, room):
        self.room = room
        self.students = []              # HAS A list of Student objects

    def add(self, student):
        self.students.append(student)

    def average(self):
        total = sum(s.marks for s in self.students)
        return total / len(self.students)

room = Classroom("Lab 2")
room.add(asha)
room.add(Student("Ravi", 68))
print(room.average())                   # 75.0
# This is called composition. Ask "IS A or HAS A?" before every
# class Child(Parent). Most relationships in real programs are HAS A.


# ==========================================================================
# THINK ABOUT IT
#   1. Without running: what is the MRO of  class Mentor(Trainer) ?
#   2. In section 4, change the class line to Artist(Dancer, Singer).
#      What prints now?
#   3. A Car has an Engine. A Car is a Vehicle. Which one is inheritance
#      and which one is composition?
#
# PRACTICE
#   Open practice/practice_03_inheritance.py
# ==========================================================================
