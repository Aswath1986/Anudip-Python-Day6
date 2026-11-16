"""
==========================================================================
 Day 6 | Practice 05 : Abstraction
==========================================================================
 After Lesson 06 and Deep Dive 05.

 Before typing, write down:
   WHAT must every shape be able to do?   HOW does each one do it?

 Finish the TODOs, then run:  python practice_05_abstraction.py
==========================================================================
"""
from abc import ABC, abstractmethod
from checker import check, raises, summary


# --------------------------------------------------------------------------
# Task 1. The contract
# --------------------------------------------------------------------------
# TODO: make Shape an abstract class (inherit from ABC).
# TODO: area() and perimeter() are abstract methods.
# TODO: describe() is an ordinary method written here, once. It returns
#       "<ClassName>: area <area>, perimeter <perimeter>"
#       Hint: type(self).__name__
class Shape:
    pass


# --------------------------------------------------------------------------
# Task 2. Two classes that keep the contract
# --------------------------------------------------------------------------
# TODO: Rectangle(length, width)
class Rectangle(Shape):
    pass


# TODO: Square(side). A Square IS A Rectangle whose length and width are
#       equal, so it needs only an __init__ that calls super().__init__.
class Square(Rectangle):
    pass


# --------------------------------------------------------------------------
# Task 3. A caller that knows only the contract
# --------------------------------------------------------------------------
# TODO: return the total area of every shape in the list.
def total_area(shapes):
    pass


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
print("Task 1")
check("Shape is abstract", lambda: issubclass(Shape, ABC) and raises(TypeError, lambda: Shape()))
class Blob(Shape):                      # keeps only half the contract
    def area(self):
        return 1
check("a half-finished child is refused",
      lambda: issubclass(Shape, ABC) and raises(TypeError, lambda: Blob()))

print("Task 2")
check("Rectangle area", lambda: Rectangle(3, 5).area() == 15)
check("Rectangle perimeter", lambda: Rectangle(3, 5).perimeter() == 16)
check("Square reuses Rectangle", lambda: Square(4).area() == 16 and "area" not in Square.__dict__)
check("describe() written once in Shape",
      lambda: Square(4).describe() == "Square: area 16, perimeter 16"
      and "describe" not in Rectangle.__dict__)

print("Task 3")
check("total_area", lambda: total_area([Rectangle(3, 5), Square(4), Square(1)]) == 32)

summary()
