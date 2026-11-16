"""
==========================================================================
 Day 6 | Practice 01 : Class and self
==========================================================================
 After Lessons 01-02 and Deep Dive 01.

 Before typing, write down for each class:
   What data does one object hold?   What rules belong with that data?

 Finish the TODOs, then run:  python practice_01_class_and_self.py
 Every line of the report should say PASS.
==========================================================================
"""
from checker import check, summary


# --------------------------------------------------------------------------
# Task 1. A Book
# --------------------------------------------------------------------------
# TODO: __init__ takes title and price and stores both.
# TODO: price_with_gst() returns the price plus 5 percent.
# TODO: __str__ returns text like  "Python Basics: Rs 200"
class Book:
    pass


# --------------------------------------------------------------------------
# Task 2. A Counter with a shared step
# --------------------------------------------------------------------------
# TODO: class attribute step = 1
# TODO: __init__ sets self.value to 0
# TODO: tick() adds Counter.step to self.value
class Counter:
    pass


# --------------------------------------------------------------------------
# Task 3. Fix the trap (Deep Dive 01, section 5)
# --------------------------------------------------------------------------
# TODO: each Team must have its OWN list of members. Change this class.
class Team:
    members = []

    def join(self, name):
        self.members.append(name)


# --------------------------------------------------------------------------
# Checks. Read them: each one is an example of how your class is used.
# --------------------------------------------------------------------------
print("Task 1")
check("Book stores title", lambda: Book("Python Basics", 200).title == "Python Basics")
check("price_with_gst", lambda: Book("Python Basics", 200).price_with_gst() == 210)
check("__str__", lambda: str(Book("Python Basics", 200)) == "Python Basics: Rs 200")

print("Task 2")
def two_counters():
    a, b = Counter(), Counter()
    a.tick()
    a.tick()
    Counter.step = 5
    b.tick()
    Counter.step = 1
    return (a.value, b.value) == (2, 5)
check("Counter starts at 0", lambda: Counter().value == 0)
check("tick uses the shared step", two_counters)

print("Task 3")
def separate_teams():
    red, blue = Team(), Team()
    red.join("Asha")
    return red.members == ["Asha"] and blue.members == []
check("each Team has its own members", separate_teams)

summary()
