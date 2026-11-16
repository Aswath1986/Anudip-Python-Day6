"""
==========================================================================
 Day 6 | Practice 03 : Inheritance
==========================================================================
 After Lesson 04 and Deep Dive 03.

 Before typing, say each relationship aloud:
   "A ___ IS A ___"  or  "A ___ HAS A ___".  Only IS A gets a parent class.

 Finish the TODOs, then run:  python practice_03_inheritance.py
==========================================================================
"""
from checker import check, summary


# --------------------------------------------------------------------------
# Task 1. Employees
# --------------------------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary

    def describe(self):
        return f"{self.name} earns {self.monthly_pay()}"


# TODO: Manager IS AN Employee with one more attribute: bonus.
#       Use super().__init__ for name and salary.
# TODO: override monthly_pay() to return the parent's answer plus bonus.
#       Do not rewrite describe().
class Manager(Employee):
    pass


# TODO: Intern IS AN Employee. An intern is paid half the salary.
#       Intern takes the same inputs as Employee, so it needs no __init__.
class Intern(Employee):
    pass


# --------------------------------------------------------------------------
# Task 2. HAS A
# --------------------------------------------------------------------------
# TODO: a Department HAS employees. Do NOT inherit from Employee.
#       __init__ takes a name and starts with an empty list.
#       hire(employee) adds one.
#       payroll() returns the total of monthly_pay() of everyone.
class Department:
    pass


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
print("Task 1")
check("Manager keeps name and salary", lambda: Manager("Latha", 50000, 8000).name == "Latha")
check("Manager pay includes bonus", lambda: Manager("Latha", 50000, 8000).monthly_pay() == 58000)
check("describe() is inherited and correct",
      lambda: Manager("Latha", 50000, 8000).describe() == "Latha earns 58000")
check("Intern is paid half, with no __init__ of its own",
      lambda: Intern("Bo", 20000).monthly_pay() == 10000 and "__init__" not in Intern.__dict__)
check("Manager IS AN Employee", lambda: isinstance(Manager("L", 1, 1), Employee))

print("Task 2")
def payroll_flow():
    dept = Department("Training")
    dept.hire(Employee("Asha", 30000))
    dept.hire(Manager("Latha", 50000, 8000))
    dept.hire(Intern("Bo", 20000))
    return dept.payroll() == 98000
check("payroll adds every kind of employee", payroll_flow)
check("Department HAS employees, it is not one",
      lambda: payroll_flow() and not issubclass(Department, Employee))

summary()
