"""
==========================================================================
 Day 6 | Practice 01 : Class and Object
==========================================================================
 After Lessons 01 and 02.   Two TODOs.

 Run :  python practice_01_class_and_object.py
 You are done when every line says PASS.
==========================================================================
"""
from checker import check, summary


class Book:
    def __init__(self, title, price):
        self.title = title
        # TODO 1: store the price too, the same way as the title.

    # TODO 2: write a method is_costly(self) that returns True when the
    #         price is more than 500, otherwise False.


check("a Book remembers its title", lambda: Book("Python Basics", 200).title == "Python Basics")
check("a Book remembers its price", lambda: Book("Python Basics", 200).price == 200)
check("a Rs 200 book is not costly", lambda: Book("Python Basics", 200).is_costly() is False)
check("a Rs 900 book is costly", lambda: Book("Atlas", 900).is_costly() is True)
summary()
