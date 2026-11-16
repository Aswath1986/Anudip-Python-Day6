"""
==========================================================================
 Day 6 | Deep Dive 04 : Polymorphism and Dunder Methods
==========================================================================
 Goes deeper than Lesson 05.

 First principle
   len(x), x + y, x == y and print(x) work on strings, lists and numbers
   for one reason: each is turned into a method call on the object.
   len(x) asks x.__len__(). x + y asks x.__add__(y). Give your class the
   same methods and Python's own tools accept your objects.
   "Dunder" is short for double underscore.

 What you will learn
   1. The built-ins are method calls in disguise
   2. __str__ and __repr__
   3. __eq__: what "equal" means for your objects
   4. __lt__: making sorted() and max() work
   5. __len__, __contains__ and __getitem__: behaving like a list
   6. Duck typing and what happens when the method is missing

 Run this file :  python deep_dive_04_polymorphism_and_dunder_methods.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Built-ins in disguise
# --------------------------------------------------------------------------
print(len("Asha"), "Asha".__len__())            # 4 4
print(2 + 3, (2).__add__(3))                    # 5 5
print("a" + "b", "a".__add__("b"))              # ab ab
# One symbol, many behaviours, because each type wrote its own method.

# --------------------------------------------------------------------------
# 2. __str__ and __repr__
# --------------------------------------------------------------------------
class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __str__(self):                  # for people: print()
        return f"Rs {self.rupees}"

    def __repr__(self):                 # for programmers: inside lists, debugging
        return f"Money({self.rupees})"

    # ---- section 3 ----
    def __eq__(self, other):
        return self.rupees == other.rupees

    # ---- section 4 ----
    def __lt__(self, other):            # lt = less than:  self < other
        return self.rupees < other.rupees

    def __add__(self, other):
        return Money(self.rupees + other.rupees)

fee = Money(500)
print(fee)                              # Rs 500
print([fee, Money(20)])                 # [Money(500), Money(20)]

# --------------------------------------------------------------------------
# 3. __eq__
# --------------------------------------------------------------------------
print(Money(100) == Money(100))         # True
print(Money(100) is Money(100))         # False   two different objects
# Day 3: == compares values, is compares identity. Without __eq__ Python
# cannot know what "same value" means for Money, so == would fall back to
# identity and say False.

# --------------------------------------------------------------------------
# 4. __lt__ and __add__
# --------------------------------------------------------------------------
prices = [Money(40), Money(10), Money(15)]
print(sorted(prices))                   # [Money(10), Money(15), Money(40)]
print(max(prices))                      # Rs 40
print(Money(40) + Money(10))            # Rs 50
# sorted() only ever asks "is a < b?". One method, and sorting works.

# --------------------------------------------------------------------------
# 5. Behaving like a list
# --------------------------------------------------------------------------
class Batch:
    def __init__(self, names):
        self._names = list(names)

    def __len__(self):                  # len(batch)
        return len(self._names)

    def __contains__(self, name):       # "Asha" in batch
        return name in self._names

    def __getitem__(self, index):       # batch[0], and also for loops
        return self._names[index]

batch = Batch(["Asha", "Ravi", "Meena"])
print(len(batch))                       # 3
print("Ravi" in batch)                  # True
print(batch[0])                         # Asha
for name in batch:                      # works because of __getitem__
    print(" ", name)

# --------------------------------------------------------------------------
# 6. Duck typing
# --------------------------------------------------------------------------
def total_length(things):
    return sum(len(thing) for thing in things)

print(total_length(["Asha", [1, 2, 3], batch]))     # 10
# A str, a list and a Batch in one call. The function never checks types.

try:
    total_length([42])
except TypeError as error:
    print("Error:", error)              # object of type 'int' has no len()
# Python checks at the moment of the call: no __len__, no len().


# ==========================================================================
# THINK ABOUT IT
#   1. Remove __repr__ from Money. What does print([fee]) show now, and
#      what does print(fee) show?
#   2. Money(100) == 100 raises an AttributeError. Why? How could __eq__
#      be written to return False instead?
#   3. Which dunder method do you think runs for  if batch:  ?
#      Test it with Batch([]).
#
# PRACTICE
#   Open practice/practice_04_polymorphism.py
# ==========================================================================
