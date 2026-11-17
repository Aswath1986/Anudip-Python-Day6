"""
==========================================================================
 Day 6 | Deep Dive 01 : What self Really Is
==========================================================================
 Goes deeper than Lessons 01 and 02.

 First principle
   Day 3: a variable is a name pointing at an object. Day 5: a function is
   an object too. A class adds only one new idea: a method is a plain
   function stored in the class, and Python passes the object in as the
   first argument. That first argument is what we call self.

 What you will learn
   1. A class is an object, and so is everything made from it
   2. asha.method() is short for Student.method(asha)
   3. Where an object keeps its data: __dict__
   4. How Python looks up a name: object first, then class
   5. The trap: a mutable class attribute is shared
   6. __init__ does not create the object, it fills it

 Run this file :  python deep_dive_01_what_self_really_is.py
==========================================================================
"""

class Student:
    centre = "Anudip"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40

# --------------------------------------------------------------------------
# 1. A class is an object
# --------------------------------------------------------------------------
print(type(Student))                    # <class 'type'>
Learner = Student                       # a second name for the same class
ravi = Learner("Ravi", 67)
print(type(ravi).__name__)              # Student

# --------------------------------------------------------------------------
# 2. The two ways to call a method
# --------------------------------------------------------------------------
asha = Student("Asha", 82)

print(asha.has_passed())                # True
print(Student.has_passed(asha))         # True    the same call, written out
# asha.has_passed()  means  "find has_passed in asha's class, pass asha in".
# So self is not a keyword. It is an ordinary parameter name that everyone
# agrees to use. This also explains a famous error message:
#
#   class Bad:
#       def hello():                    # forgot self
#           return "hi"
#   Bad().hello()
#   TypeError: hello() takes 0 positional arguments but 1 was given
#
# The "1 given" is the object that Python passed in for you.

# --------------------------------------------------------------------------
# 3. Where the data lives
# --------------------------------------------------------------------------
print(asha.__dict__)                    # {'name': 'Asha', 'marks': 82}
# An object's attributes are stored in a dict. The class of Lesson 01
# is the dict from its section 1, with rules attached.

asha.city = "Chennai"                   # attributes can be added later
print(asha.__dict__)                    # {'name': 'Asha', 'marks': 82, 'city': 'Chennai'}
# Allowed, but avoid it: set every attribute in __init__ so that all
# objects of the class have the same shape.

# --------------------------------------------------------------------------
# 4. Name lookup: object first, then class
# --------------------------------------------------------------------------
print("centre" in asha.__dict__)        # False   not stored in the object
print(asha.centre)                      # Anudip  found in the class

asha.centre = "Anudip Chennai"          # creates an INSTANCE attribute
print(asha.centre)                      # Anudip Chennai
print(ravi.centre)                      # Anudip          the class is unchanged
print(Student.centre)                   # Anudip
# Reading looks in the object, then in the class.
# Assigning through an object always writes into the object.

# --------------------------------------------------------------------------
# 5. The trap: a mutable class attribute
# --------------------------------------------------------------------------
class Batch:
    students = []                       # ONE list, shared by every Batch

    def enrol(self, name):
        self.students.append(name)      # append changes the shared list

morning = Batch()
evening = Batch()
morning.enrol("Asha")
print(evening.students)                 # ['Asha']   <- evening has no students!

class GoodBatch:
    def __init__(self):
        self.students = []              # a fresh list for each object

    def enrol(self, name):
        self.students.append(name)

morning = GoodBatch()
evening = GoodBatch()
morning.enrol("Asha")
print(evening.students)                 # []
# This is the mutable default trap of Day 5 Deep Dive 01 in new clothes.

# --------------------------------------------------------------------------
# 6. __init__ fills an object that already exists
# --------------------------------------------------------------------------
class Tracker:
    def __init__(self):
        print("  __init__ received", type(self).__name__, "object")
        self.ready = True

t = Tracker()
# Student("Asha", 82) does two things: first Python builds an empty
# Student object, then it calls __init__ with that object as self.


# ==========================================================================
# THINK ABOUT IT
#   1. In section 4, after  asha.centre = "Anudip Chennai", what does
#      asha.__dict__ contain?
#   2. Why does section 5 go wrong with append but section 4 does not go
#      wrong with = ?  (Day 3: changing an object or pointing a name.)
#   3. What will  Student.has_passed()  with no argument say? Predict the
#      exact wording of the error, then try it.
# ==========================================================================
