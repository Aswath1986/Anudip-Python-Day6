"""
A small module used by every practice file. Keep it in this folder.

check(label, test) runs test(), a function with no inputs (Day 5: a lambda).
It prints PASS when the test returns True, and NOT YET otherwise, so an
unfinished practice file still runs to the end.
"""

_results = {"pass": 0, "total": 0}


def check(label, test):
    _results["total"] += 1
    try:
        if test() is True:
            _results["pass"] += 1
            print(f"  PASS     {label}")
        else:
            print(f"  NOT YET  {label}")
    except Exception as error:
        print(f"  NOT YET  {label}   ({type(error).__name__}: {error})")


def raises(error_type, action):
    """Return True when calling action() raises error_type."""
    try:
        action()
    except error_type:
        return True
    return False


def summary():
    print(f"\n{_results['pass']} of {_results['total']} checks passed")
