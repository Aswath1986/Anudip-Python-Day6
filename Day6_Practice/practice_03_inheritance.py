"""
==========================================================================
 Day 6 | Practice 03 : Inheritance
==========================================================================
 After Lesson 04.   Two TODOs.

 Run :  python practice_03_inheritance.py
 You are done when every line says PASS.
==========================================================================
"""
from checker import check, summary


class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"I am {self.name}"


class Student(Person):
    def __init__(self, name, marks):
        # TODO 1: let the parent store the name:  super().__init__(name)
        #         then store marks yourself.
        pass


class Trainer(Person):
    # TODO 2: override intro() so that it returns
    #         "I am <name> and I am a trainer"
    pass


check("a Student gets intro() from Person", lambda: Student("Asha", 82).intro() == "I am Asha")
check("a Student has marks", lambda: Student("Asha", 82).marks == 82)
check("a Trainer has its own intro()",
      lambda: Trainer("Kumar").intro() == "I am Kumar and I am a trainer")
summary()
