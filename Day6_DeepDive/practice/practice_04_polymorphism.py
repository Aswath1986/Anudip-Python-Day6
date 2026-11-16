"""
==========================================================================
 Day 6 | Practice 04 : Polymorphism
==========================================================================
 After Lesson 05 and Deep Dive 04.

 Before typing, write down:
   What is the ONE method name that every class here must answer?

 Finish the TODOs, then run:  python practice_04_polymorphism.py
==========================================================================
"""
from checker import check, summary


# --------------------------------------------------------------------------
# Task 1. Three notifiers, one method name
# --------------------------------------------------------------------------
# TODO: each class gets send(self, message) that returns
#       "SMS: <message>", "EMAIL: <message>" or "WHATSAPP: <message>".
class Sms:
    pass

class Email:
    pass

class WhatsApp:
    pass


# TODO: return a list with the result of send(message) from every notifier.
#       No if, no type(), no isinstance().
def notify_all(notifiers, message):
    pass


# --------------------------------------------------------------------------
# Task 2. Make your class work with Python's own tools
# --------------------------------------------------------------------------
# TODO: __init__ takes metres and stores it.
# TODO: __str__   ->  "5 m"
# TODO: __eq__    ->  equal when the metres are equal
# TODO: __lt__    ->  smaller when the metres are smaller
# TODO: __add__   ->  a NEW Distance with the metres added
class Distance:
    pass


# --------------------------------------------------------------------------
# Task 3. A playlist that behaves like a list
# --------------------------------------------------------------------------
# TODO: __init__ takes a list of song names.
# TODO: make len(playlist), "song" in playlist and playlist[0] work.
class Playlist:
    pass


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
print("Task 1")
check("Sms.send", lambda: Sms().send("Hi") == "SMS: Hi")
check("notify_all", lambda: notify_all([Sms(), Email(), WhatsApp()], "Class at 9")
      == ["SMS: Class at 9", "EMAIL: Class at 9", "WHATSAPP: Class at 9"])
class Pigeon:                           # a class this file has never seen
    def send(self, message):
        return "PIGEON: " + message
check("a brand new notifier works without changes",
      lambda: notify_all([Pigeon()], "Hi") == ["PIGEON: Hi"])

print("Task 2")
check("__str__", lambda: str(Distance(5)) == "5 m")
check("__eq__", lambda: (Distance(5) == Distance(5)) is True)
check("__add__ gives a new Distance", lambda: str(Distance(5) + Distance(7)) == "12 m")
check("sorted() works", lambda: [d.metres for d in sorted([Distance(9), Distance(2), Distance(5)])] == [2, 5, 9])
check("max() works", lambda: max([Distance(9), Distance(2)]).metres == 9)

print("Task 3")
check("len()", lambda: len(Playlist(["a", "b", "c"])) == 3)
check("in", lambda: ("b" in Playlist(["a", "b"])) is True)
check("indexing", lambda: Playlist(["a", "b"])[1] == "b")
check("for loop", lambda: [s for s in Playlist(["a", "b"])] == ["a", "b"])

summary()
