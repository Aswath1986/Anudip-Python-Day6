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

## Practice

The [`practice/`](practice) folder has one exercise file per deep dive. Each file has
`TODO` comments to finish and a set of checks at the bottom.

```bash
cd Day6_DeepDive/practice
python practice_01_class_and_self.py
```

| File | Practises | Checks |
|------|-----------|--------|
| `practice_01_class_and_self.py` | a class from scratch, a class attribute, fixing the shared-list trap | 6 |
| `practice_02_encapsulation.py` | a guarded account, a validated setter, a computed property | 10 |
| `practice_03_inheritance.py` | `super()`, overriding, and a HAS A class | 7 |
| `practice_04_polymorphism.py` | one method name in three classes, dunder methods, a list-like class | 12 |
| `practice_05_abstraction.py` | an abstract class, two children, a caller that knows only the contract | 7 |

A fresh file prints `NOT YET` for every check and still runs to the end. Work on one task,
run the file, and watch the lines turn to `PASS`. The text in brackets after `NOT YET` is the
error Python raised, which tells you what to write next. The checks are also examples: read
them to see how your class is expected to be used.

`checker.py` is a small module that the practice files import. Keep it in the `practice` folder.

> Exact error messages and memory addresses (`0x7f...`) can differ between Python versions
> and computers. The behaviour does not.
