"""
==========================================================================
 Day 6 | Practice 05 : Abstraction
==========================================================================
 After Lesson 06.   Two TODOs.

 Run :  python practice_05_abstraction.py
 You are done when every line says PASS.
==========================================================================
"""
from abc import ABC, abstractmethod
from checker import check, summary


class Shape(ABC):                       # the contract: every shape has area()
    @abstractmethod
    def area(self):
        pass


class Square(Shape):                    # already written: use it as a model
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        # TODO 1: store length and width.
        pass

    # TODO 2: write area(self) that returns length times width.
    #         Until you do, Python refuses to make a Rectangle.


check("a Square of side 4 has area 16", lambda: Square(4).area() == 16)
check("a Rectangle can be made", lambda: isinstance(Rectangle(3, 5), Shape))
check("a 3 by 5 Rectangle has area 15", lambda: Rectangle(3, 5).area() == 15)
summary()
