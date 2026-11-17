# Day 6 lesson plan: closing Day 5, then classes and the four pillars

For the facilitator. Total time: about 3 hours including a break.
The class has completed Day 5 up to recursion (Lesson 05). Day 6 first finishes
Day 5, then moves to object-oriented programming.

Students follow the files in [`Day6_Structured`](Day6_Structured); the
[`Day6_Practice`](Day6_Practice) folder has a five-minute exercise for each concept, and
the [`Day6_DeepDive`](Day6_DeepDive) folder is for self-study afterwards.

## The first-principles method, light version

For every topic, ask three questions in this order. Do not show syntax until
the class has answered the first one.

1. **What is the problem?** Show code that is awkward or unsafe without the feature.
2. **What is the smallest idea that fixes it?** Say it in one plain sentence.
3. **What does it look like in Python?** Only now show the syntax, and predict before running.

Each structured lesson opens with a "First principle" paragraph that gives you
questions 1 and 2 ready to read out.

## Timings

### Part 1: closing Day 5 (files in the Day 5 repository, `Day5_Structured`)

| Time | Lesson | Ask the class first | Then |
|---|---|---|---|
| 0:00–0:05 | Recap | "Yesterday a function called itself. What two parts did it need?" | Base case, recursive case. State today's thread: reuse more with less typing. |
| 0:05–0:20 | Day 5, 06 Lambda | "Sort these names by their last letter. `sorted` needs a function. Is it worth a `def`?" | `lambda` shape; `sorted` and `max` with `key`. One expression only. |
| 0:20–0:35 | Day 5, 07 map, filter, reduce | Write three loops on the board (add 5 to each, keep the passes, total). "What is the one-word job of each loop?" | Change, keep, combine. Loop way first, then the function way. |
| 0:35–0:55 | Day 5, 08 Modules and 09 Libraries | "You wrote `add_gst` yesterday. Today another program needs it. What do you do?" | `import` three ways, `__name__`, then a short tour of `math`, `random`, `datetime` and what `pip install` does. |
| 0:55–1:00 | Day 6, 00 Warm-up | Run the file as a two-minute recap. Read section 4 aloud. | "A function reuses a rule. How do we reuse data together with its rules?" |
| 1:00–1:10 | Break | | |

### Part 2: Day 6 (files in `Day6_Structured`)

| Time | Lesson | Ask the class first | Then |
|---|---|---|---|
| 1:10–1:35 | 01 Class and object | Show the two dicts in section 1. "Ravi's dict has a typo. When does Python tell us?" | Blueprint and object. Trace `Student("Asha", 82)` on the board: empty object, then `__init__` fills it. `asha.has_passed()` passes asha in as `self`. |
| 1:35–1:50 | 02 Attributes and methods | "The pass mark changes from 40 to 35. With 500 student objects, how many places must change?" | Class attribute against instance attribute; `__str__`; objects in a list with `max` and `filter`. |
| 1:50–2:05 | 03 Encapsulation | Run `acc.balance = -5000`. "Who is responsible for stopping this?" | Methods as the only door, `_` as a promise, `__`, `@property`. |
| 2:05–2:20 | 04 Inheritance | Show the Student and Trainer classes side by side in section 1. "Add a phone number. How many edits?" | Parent, child, `super()`, overriding. Finish with the IS A test. |
| 2:20–2:35 | 05 Polymorphism | "`len` works on a string and on a list. How can one function do two jobs?" Then show `pay_old`. "Add wallet payments. What must we edit?" | Same method name in each class; `checkout` never changes. |
| 2:35–2:50 | 06 Abstraction | "You switched on the fan today. Who can explain the wiring?" Then: "In Lesson 05, what forced every class to have `pay`?" | Nothing did. `ABC` and `@abstractmethod` make it a contract. Run the `BrokenCash` case and read the message. |
| 2:50–3:00 | 07 Mini project and close | "Find each of today's ideas in these two files." | Students point to the line for each idea. Assign the practice folder. The deep dives are optional. |

## How to run each lesson

1. Read the First principle paragraph aloud and ask the question from the table.
2. Students run the file and read the output against the comments.
3. Remove the `#` from one commented error line, run, and read the message aloud.
4. Do the **PREDICT** block together: hands up for each answer before anyone runs it.
5. Leave **TRY IT YOURSELF** for pair practice or homework.

## Where time will slip

- **`self`** is the hardest idea of the day. Keep saying "self is the object the method was
  called on. `asha.has_passed()` means self is asha". Draw two objects on the board, each
  with its own name and marks, and point at the one being used.
- **`__init__`** looks like magic. Say "it runs once, when the object is made, to fill it".
  Do not explain other dunder methods here; `__str__` in Lesson 02 is enough.
- **Encapsulation and abstraction** get mixed up. One line each: encapsulation protects the
  *data*, abstraction hides the *steps* and fixes the *method names*.
- **If Part 1 runs long,** shorten the library tour to `math` and `random`, and skip Day 6
  Lesson 00.
- **If you are 15 minutes behind after Lesson 03,** teach Lesson 05 up to section 3 only,
  and in Lesson 06 teach sections 2 to 4 only. Lesson 07 can become homework reading.
- **If the class needs two sessions,** stop after Lesson 03. Lessons 04 to 07 make a
  complete second session that starts from the same `Person` and payment examples.

## Common mistakes to watch for

| Students write | What to ask them |
|---|---|
| `def has_passed():` with no `self` | "Python passes the object in. Where will it go?" |
| `marks >= 40` inside a method, without `self.` | "Which student's marks? There may be fifty objects." |
| `def _init_(self):` or `def init(self):` | "Count the underscores. Did your object get its name?" |
| `Student.has_passed()` | "Which student are you asking about?" |
| `asha.has_passed` with no brackets | "Day 5: what is a function name without brackets?" |
| A child `__init__` with no `super().__init__(...)` | "Who sets `name` now?" |
| `class Classroom(Student)` | "Say it aloud: a classroom IS A student?" |
| `p = Payment("Asha")` on an abstract class | "Can you pay with 'a payment', or only with UPI, card or cash?" |
| `print(asha)` showing `<__main__.Student object at ...>` | "Which method tells `print` what to show?" |

## Practice: always the light one

Practice is kept deliberately small, so that every student finishes it.
[`Day6_Practice`](Day6_Practice) has one file per concept. Each file needs only
the structured lesson, has two TODOs beside a worked model, and prints `PASS`
or `NOT YET`, so students see their own progress without a facilitator.

| Practice file | After lesson | Time |
|---|---|---|
| `practice_01_class_and_object.py` | 01–02 | 5 min |
| `practice_02_encapsulation.py` | 03 | 5 min |
| `practice_03_inheritance.py` | 04 | 5 min |
| `practice_04_polymorphism.py` | 05 | 5 min |
| `practice_05_abstraction.py` | 06 | 5 min |

If a lesson finishes early, do its practice file in class; otherwise all five
are homework. The answers, with the mistake to expect in each file, are in an
encrypted answer key; see [`Facilitator/README.md`](Facilitator/README.md) for how to open it.

## Self-study: the deep dives

Optional, and separate from practice. They explain why; they set no exercises
beyond THINK ABOUT IT questions.

| Deep dive | Follow-up to | Why a student would open it |
|---|---|---|
| 01 What self really is | Lessons 01–02 | To read "takes 0 positional arguments but 1 was given" and know the cause |
| 02 Guarding data with property | Lesson 03 | To validate on plain assignment and raise errors instead of printing |
| 03 How inheritance finds a method | Lesson 04 | To know which method runs, and when not to inherit |
| 04 Polymorphism and dunder methods | Lesson 05 | To make their own class work with `len`, `==`, `+`, `sorted` and `for` |
| 05 Abstraction as a contract | Lesson 06 | To see how teams split work, and the four pillars working together |

## Checking understanding

Ask these at the close or at the start of the next session. A student who can
answer in plain words has understood the principle, not just the syntax.

1. What is the difference between a class and an object?
2. In `asha.has_passed()`, what is `self`?
3. Give one fact about students that belongs in a class attribute and one that belongs in an instance attribute.
4. Why is `acc.deposit(500)` safer than `acc.balance = acc.balance + 500`?
5. What does `super().__init__(name, city)` do?
6. `checkout(method, amount)` works for UPI, card and cash. What must every one of those classes have?
7. What happens when you make an object of a class that has an abstract method left unwritten?
8. Encapsulation and abstraction both hide something. What does each one hide?
