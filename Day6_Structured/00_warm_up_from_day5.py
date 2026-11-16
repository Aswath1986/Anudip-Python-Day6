"""
==========================================================================
 Day 6 | Lesson 00 : Warm-up, Closing Day 5
==========================================================================
 First principle
   Day 5 was about reuse: write a rule once, use it many times.
   A function reuses a rule. A module reuses a file of functions.
   Today we ask the next question: how do we reuse DATA and its rules
   together?

 What you will revise
   1. lambda: a one-expression function
   2. map, filter, reduce: change, keep, combine
   3. Modules and libraries: import what already exists

 The full lessons are in the Day 5 repository:
   Day5_Structured/06_lambda_functions.py  to  09_libraries.py

 Run this file :  python 00_warm_up_from_day5.py
==========================================================================
"""
from functools import reduce            # a tool from the standard library
import math                             # a whole module

# --------------------------------------------------------------------------
# 1. lambda
# --------------------------------------------------------------------------
add_gst = lambda price: price * 1.05
print(add_gst(100))                     # 105.0

students = [("Asha", 82), ("Ravi", 67), ("Meena", 91)]
print(sorted(students, key=lambda s: s[1]))     # sorted by marks

# --------------------------------------------------------------------------
# 2. map (change), filter (keep), reduce (combine)
# --------------------------------------------------------------------------
marks = [82, 67, 91, 35]

print(list(map(lambda m: m + 5, marks)))        # [87, 72, 96, 40]
print(list(filter(lambda m: m >= 40, marks)))   # [82, 67, 91]
print(reduce(lambda total, m: total + m, marks, 0))     # 275

# --------------------------------------------------------------------------
# 3. Modules and libraries
# --------------------------------------------------------------------------
print(math.sqrt(49))                    # 7.0
# A module is one .py file. A library is a collection of modules that
# someone has already written and tested for you.

# --------------------------------------------------------------------------
# 4. The question that opens today
# --------------------------------------------------------------------------
# A student is more than one value: a name, marks, a city.
# The rules about a student (is this a pass? add grace marks) are functions.
# Right now the data sits in one place and the rules sit in another.
# Lesson 01 puts them together.


# ==========================================================================
# PREDICT before you run!
#
#   nums = [1, 2, 3, 4]
#   print(list(map(lambda n: n * n, nums)))
#   print(list(filter(lambda n: n % 2 == 0, nums)))
#   print(reduce(lambda a, b: a * b, nums, 1))
#
# TRY IT YOURSELF
#   1. From ["pen", "notebook", "bag"], make a list of the lengths with map.
#   2. Keep only the names longer than 3 letters with filter.
#   3. Import random and print random.choice(["Asha", "Ravi", "Meena"]).
# ==========================================================================
