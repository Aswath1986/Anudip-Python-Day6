# Day 6 – Deep Dive Sessions

Take these **after** the structured lessons, in your own time. Each deep dive picks one idea
from class and rebuilds it from first principles, so you see *why* Python behaves that way.

| # | File | Goes deeper into | Key ideas |
|---|------|------------------|-----------|
| 01 | `deep_dive_01_what_self_really_is.py` | Lessons 01–02 | `asha.method()` is `Student.method(asha)`, `__dict__`, object-then-class lookup, the shared mutable class attribute trap |
| 02 | `deep_dive_02_guarding_data_with_property.py` | Lesson 03 | name mangling, private as an agreement, `@property` with a setter, raising instead of printing, computed properties |
| 03 | `deep_dive_03_how_inheritance_finds_a_method.py` | Lesson 04 | the search path (`__mro__`), `object`, forgetting `super()`, two parents, IS A against HAS A |
| 04 | `deep_dive_04_polymorphism_and_dunder_methods.py` | Lesson 05 | `len()` and `+` as method calls, `__str__`, `__repr__`, `__eq__`, `__lt__`, behaving like a list, duck typing |
| 05 | `deep_dive_05_abstraction_as_a_contract.py` | Lesson 06 | failing late against failing early, the template method, swapping an implementation, the four pillars together |

Every file ends with **THINK ABOUT IT** questions. Several of them connect back to Day 3
(objects, names and mutability) and Day 5 (functions are objects), because a class is built
from those same ideas.

```bash
cd Day6_DeepDive
python deep_dive_01_what_self_really_is.py
```

Looking for short exercises? The light practice files are in [`../Day6_Practice`](../Day6_Practice).

> Exact error messages and memory addresses (`0x7f...`) can differ between Python versions
> and computers. The behaviour does not.
