"""
==========================================================================
 Day 6 | Practice 02 : Encapsulation
==========================================================================
 After Lesson 03 and Deep Dive 02.

 Before typing, write down:
   Which values must never be wrong?   Which single method may change them?

 Finish the TODOs, then run:  python practice_02_encapsulation.py
==========================================================================
"""
from checker import check, raises, summary


# --------------------------------------------------------------------------
# Task 1. A bank account that cannot go wrong
# --------------------------------------------------------------------------
# TODO: __init__ takes owner and an opening balance, stored as _balance.
# TODO: deposit(amount) adds it. Raise ValueError when amount <= 0.
# TODO: withdraw(amount) subtracts it. Raise ValueError when amount <= 0
#       or when amount is more than the balance.
# TODO: a read-only @property called balance.
class Account:
    pass


# --------------------------------------------------------------------------
# Task 2. A thermostat with a validated setter
# --------------------------------------------------------------------------
# TODO: a property temperature with a setter.
#       Allowed range is 16 to 30. Outside it, raise ValueError.
# TODO: __init__ takes the starting temperature and uses the same check.
class Thermostat:
    pass


# --------------------------------------------------------------------------
# Task 3. A computed property
# --------------------------------------------------------------------------
# TODO: __init__ takes a list of marks and keeps a COPY in _marks.
# TODO: add(mark) appends one mark.
# TODO: a property average that is calculated, never stored.
#       Return 0 when there are no marks.
class MarkSheet:
    pass


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
print("Task 1")
def account_flow():
    acc = Account("Asha", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    return acc.balance == 1200
check("deposit and withdraw", account_flow)
check("negative deposit is refused", lambda: raises(ValueError, lambda: Account("A", 100).deposit(-5)))
check("overdraw is refused", lambda: raises(ValueError, lambda: Account("A", 100).withdraw(500)))
def set_balance():
    Account("A", 100).balance = 999
check("balance cannot be assigned", lambda: raises(AttributeError, set_balance))

print("Task 2")
def thermostat_flow():
    t = Thermostat(24)
    t.temperature = 18
    return t.temperature == 18
def too_hot():
    Thermostat(24).temperature = 45
check("valid temperature is accepted", thermostat_flow)
check("45 is refused", lambda: raises(ValueError, too_hot))
check("bad starting value is refused", lambda: raises(ValueError, lambda: Thermostat(5)))

print("Task 3")
def sheet_flow():
    sheet = MarkSheet([80, 90])
    first = sheet.average
    sheet.add(40)
    return (first, sheet.average) == (85, 70)
def copy_kept():
    marks = [50]
    sheet = MarkSheet(marks)
    marks.append(100)                   # changing the outside list
    return sheet.average == 50
check("average follows the marks", sheet_flow)
check("empty sheet averages 0", lambda: MarkSheet([]).average == 0)
check("the sheet keeps its own copy", copy_kept)

summary()
