# Day 6 – Structured Lessons

**Topic: closing Day 5, then classes and the four pillars of object-oriented programming.**
Go through the files **in number order**. Each lesson uses only what the lessons before it taught.

Every lesson opens with a **First principle**: the problem that made the feature necessary.
Read it before the code. If you can say the problem in your own words, the syntax is easy to remember.

| # | File | Concept | The problem it solves |
|---|------|---------|-----------------------|
| 00 | `00_warm_up_from_day5.py` | recap of `lambda`, `map`, `filter`, `reduce`, `import` | Closing Day 5 and asking today's question |
| 01 | `01_class_and_object.py` | `class`, `__init__`, `self`, attributes, methods | Data and its rules live in different places |
| 02 | `02_attributes_and_methods.py` | instance and class attributes, `__str__` | A shared fact repeated inside every object |
| 03 | `03_encapsulation.py` | `_name`, `__name`, methods as the door, `@property` | Anyone can put a wrong value into the data |
| 04 | `04_inheritance.py` | parent and child, `super()`, overriding, `isinstance` | Two classes repeat the same code |
| 05 | `05_polymorphism.py` | one method name in many classes, duck typing, `__len__`, `__add__` | An `if / elif` chain on type |
| 06 | `06_abstraction.py` | `ABC`, `@abstractmethod`, hiding the steps | Nothing forces a class to provide a method |
| 07 | `07_mini_project_canteen_orders.py` | everything above in one program | Putting it together |

`canteen_models.py` is a small module that Lesson 07 imports. Keep it in this folder.

## How each lesson is laid out

1. **First principle**: the problem, in plain words.
2. **What you will learn**: the goals for the lesson.
3. **Numbered sections**: short explanations followed by code you can run.
4. **PREDICT before you run!**: write down what you expect, then check by running it.
5. **TRY IT YOURSELF**: small exercises to practise.

## Running a lesson

```bash
cd Day6_Structured
python 01_class_and_object.py
```

Lines that are commented out with an error name beside them (for example
`# print(locker.__pin)   # AttributeError`) are there to be tried: remove the `#`,
run, read the message, then put the `#` back.

When you finish, go on to the deep dives in [`../Day6_DeepDive`](../Day6_DeepDive).
The facilitator's timings are in [`../LESSON_PLAN.md`](../LESSON_PLAN.md).
