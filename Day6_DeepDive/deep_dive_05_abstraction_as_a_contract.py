"""
==========================================================================
 Day 6 | Deep Dive 05 : Abstraction as a Contract
==========================================================================
 Goes deeper than Lesson 06.

 First principle
   A large program is written by many people. The person who writes the
   billing screen and the person who writes "pay by UPI" must agree on
   one thing only: the method names and what they return. That agreement
   is an INTERFACE. Code written against the interface keeps working
   when the classes behind it are replaced.

 What you will learn
   1. A contract without ABC, and how late it fails
   2. The same contract with ABC, and how early it fails
   3. Abstract classes can carry finished code: the template method
   4. Swapping the implementation without touching the caller
   5. The four pillars in one picture

 Run this file :  python deep_dive_05_abstraction_as_a_contract.py
==========================================================================
"""
from abc import ABC, abstractmethod

# --------------------------------------------------------------------------
# 1. A contract kept by hand
# --------------------------------------------------------------------------
class ManualStorage:
    def save(self, key, value):
        raise NotImplementedError("child class must write save()")

class ForgetfulStorage(ManualStorage):
    pass                                # forgot save()

store = ForgetfulStorage()              # no error yet
try:
    store.save("asha", 82)
except NotImplementedError as error:
    print("Late error:", error)
# It works, but the mistake appears only when save() is finally called.

# --------------------------------------------------------------------------
# 2. A contract checked by Python
# --------------------------------------------------------------------------
class Storage(ABC):
    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def load(self, key):
        pass

class HalfStorage(Storage):
    def save(self, key, value):
        pass                            # load() is missing

try:
    HalfStorage()
except TypeError as error:
    print("Early error:", error)
# The error names the missing method, at the line that makes the object.

# --------------------------------------------------------------------------
# 3. The template method: fixed steps, one open slot
# --------------------------------------------------------------------------
class Report(ABC):
    def build(self, students):          # finished code in the abstract class
        lines = [self.heading()]
        for name, marks in students:
            lines.append(self.line(name, marks))
        return "\n".join(lines)

    def heading(self):                  # a default that a child may override
        return "REPORT"

    @abstractmethod
    def line(self, name, marks):        # the slot every child must fill
        pass

class PlainReport(Report):
    def line(self, name, marks):
        return f"{name}: {marks}"

class StarReport(Report):
    def heading(self):
        return "STAR REPORT"

    def line(self, name, marks):
        return f"{name:<6}{'*' * (marks // 20)}"

data = [("Asha", 82), ("Ravi", 67)]
print(PlainReport().build(data))
print(StarReport().build(data))
# build() is written once. Each child supplies only the part that differs.
# Abstraction, inheritance and polymorphism working together.

# --------------------------------------------------------------------------
# 4. Swap the implementation, keep the caller
# --------------------------------------------------------------------------
class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def load(self, key):
        return self._data.get(key)

class LoudStorage(MemoryStorage):
    def save(self, key, value):
        print(f"  saving {key}")
        super().save(key, value)


def record_marks(storage, name, marks): # knows only the Storage contract
    storage.save(name, marks)
    return storage.load(name)

print(record_marks(MemoryStorage(), "Asha", 82))    # 82
print(record_marks(LoudStorage(), "Ravi", 67))      # saving Ravi, then 67
# Tomorrow a FileStorage or a DatabaseStorage can be passed in.
# record_marks() will not change by one character.

# --------------------------------------------------------------------------
# 5. The four pillars together
# --------------------------------------------------------------------------
#   Encapsulation   _data is touched only by save() and load()
#   Abstraction     Storage says WHAT: save and load
#   Inheritance     LoudStorage reuses MemoryStorage
#   Polymorphism    record_marks() works with any Storage
#
# They are four views of one goal: change one part of a program without
# breaking the rest.


# ==========================================================================
# THINK ABOUT IT
#   1. Section 1 fails late and section 2 fails early. Why does "early"
#      matter more as a program grows?
#   2. open() gives you an object with read() and write(), for a text
#      file, a CSV file or a file on another computer. Where is the
#      abstraction?
#   3. Can an abstract class have an __init__? Look at Payment in
#      Lesson 06 before you answer.
#
# PRACTICE
#   Open practice/practice_05_abstraction.py
# ==========================================================================
