"""
==========================================================================
 Day 6 | Practice 04 : Polymorphism
==========================================================================
 After Lesson 05.   Two TODOs.

 Run :  python practice_04_polymorphism.py
 You are done when every line says PASS.
==========================================================================
"""
from checker import check, summary


class Dog:
    def speak(self):                    # already written: use it as a model
        return "Woof"


class Cat:
    # TODO 1: a speak method that returns "Meow"
    pass


class Cow:
    # TODO 2: a speak method that returns "Moo"
    pass


def all_sounds(animals):                # do not change this function
    sounds = []
    for animal in animals:
        sounds.append(animal.speak())   # one line for every kind of animal
    return sounds


check("a Cat says Meow", lambda: Cat().speak() == "Meow")
check("a Cow says Moo", lambda: Cow().speak() == "Moo")
check("one loop, three kinds of animal",
      lambda: all_sounds([Dog(), Cat(), Cow()]) == ["Woof", "Meow", "Moo"])
summary()
