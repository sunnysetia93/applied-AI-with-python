# Python for AI Roadmap

A practical, trackable roadmap for learning **Python for AI** from a JavaScript-friendly beginner/intermediate perspective.

This document is the shared source of truth for the Python-for-AI class flow. We will use it to:
- track progress lecture by lecture
- keep a clean record of what has already been covered
- decide what to study next
- build Python instincts that are useful for AI, ML, automation, and real projects

---

## How We’ll Use This Roadmap

### Learning style
- **Default pace:** 1 lecture per day
- **Bias:** practical understanding over theory-first overload
- **Approach:** concept -> example -> small code exercise -> recap
- **Special lens:** avoid writing “JavaScript in Python”; learn the Pythonic way

### Recommended lecture format
For each lecture, we should try to cover:
1. **Concepts** — what the syntax or idea means
2. **Python gotchas** — what commonly trips people up
3. **Examples** — short, runnable examples
4. **Exercise** — one or two practice tasks
5. **Notes** — key rules worth remembering

### Status legend
- `[ ]` Not started
- `[~]` In progress
- `[x]` Done
- `[*]` Needs revision / revisit

---

## Overall Outcomes

By the end of this roadmap, the learner should be able to:
- read and write Python comfortably without constantly translating from JavaScript
- understand Python data types, control flow, functions, and error patterns clearly
- use collections, iteration, comprehensions, and modules confidently
- write cleaner, more Pythonic code
- debug common Python mistakes quickly
- understand file handling, environments, packages, and project structure
- build a strong enough Python foundation for NumPy, pandas, ML, APIs, automation, and AI tooling

---

# Phase 0 — Orientation + Core Syntax

**Objective:** get comfortable with core Python syntax and mental model differences.

## Lectures
- [x] **L01. Python basics for an AI learner**
  - Outcome: understand Python operators, conditionals, truthiness/falsiness, equality vs identity, and common collection basics.
  - Exercise: predict outputs for small Python snippets involving `if`, lists, dicts, `None`, and `==` vs `is`.
  - Notes: Covered in `python-for-ai/lecture-1/notes-1.md`. Also included common errors like `KeyError`, `IndexError`, `TypeError`, `ValueError`, and `NameError`, plus copy-vs-reference traps and data-structure basics.

- [x] **L02. Functions, lists, dicts, and debugging like a Pythonista**
  - Outcome: write small functions cleanly, use lists/dicts confidently, and debug beginner Python errors faster.
  - Exercise: write small utility functions, fix broken snippets, and improve “JS-style Python” into cleaner Python.
  - Notes: Covered on 2026-03-13. Included `return` vs `print`, list and dict basics, `IndexError`/`KeyError`, debugging mindset, shared-reference bugs, and the mutable default argument trap.

- [ ] **L03. Strings, slicing, and everyday built-ins**
  - Outcome: work comfortably with strings, indexing, slicing, `len`, `sum`, `sorted`, `min`, `max`, and membership checks.
  - Exercise: solve short string/data cleanup tasks.

- [ ] **L04. Loops, `range`, `enumerate`, and iteration patterns**
  - Outcome: use `for` loops naturally in Python and avoid awkward C/JS loop habits.
  - Exercise: loop through lists, dicts, and strings using idiomatic Python.

- [ ] **L05. Mini checkpoint 1**
  - Outcome: reinforce syntax, truthiness, collections, and basic control flow.
  - Exercise: mixed practice set with output prediction + short coding tasks.

### Phase checkpoint
- Can read simple Python without hesitation.
- Can explain truthiness, `==` vs `is`, and basic collection behavior.
- Can write and call simple functions.

---

# Phase 1 — Core Python Building Blocks

**Objective:** become comfortable writing real Python instead of isolated snippets.

## Lectures
- [ ] **L06. Functions properly: parameters, return values, scope**
  - Outcome: understand function definitions, local scope, defaults, and return behavior.
  - Exercise: build 3 small helper functions.

- [ ] **L07. Mutable vs immutable objects**
  - Outcome: understand why lists/dicts behave differently from strings/tuples/ints.
  - Exercise: debug mutation bugs and shared-reference mistakes.

- [ ] **L08. List methods, dict methods, set basics**
  - Outcome: use built-in collection tools confidently.
  - Exercise: transform and query collections with common methods.

- [ ] **L09. Tuple unpacking and practical assignment patterns**
  - Outcome: write cleaner assignment code using unpacking.
  - Exercise: swap values, unpack loops, and handle grouped returns.

- [ ] **L10. Errors and exceptions**
  - Outcome: understand common exception types and how to read tracebacks.
  - Exercise: diagnose and fix broken code examples.

- [ ] **L11. Mini checkpoint 2**
  - Outcome: reinforce functions, mutability, methods, and debugging.
  - Exercise: mixed coding challenge.

### Phase checkpoint
- Can explain mutability clearly.
- Can debug common beginner mistakes without panic.
- Can choose the right collection for the job.

---

# Phase 2 — Writing More Pythonic Code

**Objective:** shift from “it works” to “this looks like Python.”

## Lectures
- [ ] **L12. Comprehensions: list, dict, and set**
  - Outcome: understand and write simple comprehensions cleanly.
  - Exercise: convert loops into comprehensions where appropriate.

- [ ] **L13. `any`, `all`, `zip`, `enumerate`, and other power tools**
  - Outcome: reduce noisy code with useful built-ins.
  - Exercise: refactor repetitive code into cleaner Python.

- [ ] **L14. Sorting with `key=` and lambda basics**
  - Outcome: sort strings, numbers, and dict-backed data properly.
  - Exercise: sort students/products/logs by different fields.

- [ ] **L15. Common anti-patterns from a JS brain**
  - Outcome: spot overly verbose or awkward Python habits.
  - Exercise: rewrite JS-style Python into more idiomatic Python.

- [ ] **L16. Mini checkpoint 3**
  - Outcome: strengthen fluency with common Pythonic patterns.
  - Exercise: style cleanup challenge.

### Phase checkpoint
- Can recognize cleaner vs clunky Python.
- Can use built-ins and comprehensions without overcomplicating code.

---

# Phase 3 — Modules, Files, and Real Project Shape

**Objective:** move from toy snippets to code that lives in files and projects.

## Lectures
- [ ] **L17. Imports, modules, and file organization**
  - Outcome: understand how Python code is split across files.
  - Exercise: break one file into reusable modules.

- [ ] **L18. Reading and writing files**
  - Outcome: handle text files safely with `with open(...)`.
  - Exercise: read a file, process it, and write output.

- [ ] **L19. Paths and `pathlib` basics**
  - Outcome: work with files in a cleaner, modern Python way.
  - Exercise: inspect and manipulate a small folder structure.

- [ ] **L20. Virtual environments and packages**
  - Outcome: understand `venv`, package installation, and isolated Python setups.
  - Exercise: create a small environment and install one package.

- [ ] **L21. `pip`, requirements, and reproducibility basics**
  - Outcome: know how dependencies are managed.
  - Exercise: record dependencies for a small project.

### Phase checkpoint
- Can structure a small Python project.
- Can manage files and packages without confusion.

---

# Phase 4 — Python for Data and AI Foundations

**Objective:** prepare the jump from pure Python into AI/ML tooling.

## Lectures
- [ ] **L22. Why NumPy exists**
  - Outcome: understand why plain Python lists are not enough for numerical work at scale.
  - Exercise: compare list thinking vs array thinking conceptually.

- [ ] **L23. NumPy arrays, shapes, and vectorized thinking**
  - Outcome: build intuition for arrays and dimensions.
  - Exercise: create and inspect simple arrays.

- [ ] **L24. pandas basics: Series and DataFrames**
  - Outcome: understand table-like data in Python.
  - Exercise: load and inspect a tiny dataset.

- [ ] **L25. Filtering, selecting, and basic data cleaning**
  - Outcome: perform basic tabular data operations.
  - Exercise: clean a small CSV.

- [ ] **L26. Mini checkpoint 4**
  - Outcome: connect Python basics to AI/data tooling.
  - Exercise: small task using Python + pandas/NumPy basics.

### Phase checkpoint
- Can understand why Python is popular for AI.
- Can read beginner-level NumPy/pandas code.

---

# Phase 5 — Python for Automation, APIs, and AI Workflows

**Objective:** use Python in the kinds of tasks that show up around modern AI work.

## Lectures
- [ ] **L27. JSON, dictionaries, and API-shaped data**
  - Outcome: work confidently with nested JSON-like structures.
  - Exercise: extract values from nested API responses.

- [ ] **L28. `requests` / HTTP basics**
  - Outcome: understand how Python calls APIs.
  - Exercise: make a simple API request and inspect the response.

- [ ] **L29. Environment variables and secrets hygiene**
  - Outcome: keep credentials out of code.
  - Exercise: load config safely from environment variables.

- [ ] **L30. Basic scripting for AI workflows**
  - Outcome: write small scripts to prepare prompts, process files, or transform outputs.
  - Exercise: build a tiny automation script.

- [ ] **L31. Working with CSV, JSON, and text for AI pipelines**
  - Outcome: move data between common file formats.
  - Exercise: convert one format to another.

### Phase checkpoint
- Can write useful Python scripts around AI tools and APIs.
- Can safely handle config and structured data.

---

# Phase 6 — Practice, Debugging, and Project Readiness

**Objective:** consolidate the foundation into confidence.

## Lectures
- [ ] **L32. Reading tracebacks calmly**
  - Outcome: break down Python errors step by step.
  - Exercise: debug several failing snippets.

- [ ] **L33. Refactoring beginner code**
  - Outcome: improve clarity, naming, and structure.
  - Exercise: clean up messy code.

- [ ] **L34. Small project 1: CLI utility**
  - Outcome: build a tiny useful command-line Python tool.
  - Exercise: complete and run the project.

- [ ] **L35. Small project 2: data mini-task**
  - Outcome: read a file, process data, and output results.
  - Exercise: finish a beginner-friendly data workflow.

- [ ] **L36. Final review + next-step bridge into AI/ML**
  - Outcome: identify what is strong, what needs review, and what to study next.
  - Exercise: build a personal “Python for AI next steps” plan.

### Phase checkpoint
- Can build and debug small Python scripts independently.
- Is ready to move deeper into data, ML, or applied AI implementation.

---

# Suggested Practice Tracks

These can run alongside the lectures.

- [ ] **Track A: Output prediction drills**
  - Build fast Python instincts by predicting outputs and errors.

- [ ] **Track B: Rewrite JS-style code into Pythonic code**
  - Improve style and readability.

- [ ] **Track C: Tiny utilities**
  - Build mini scripts like text cleaners, JSON formatters, list/dict helpers, and file processors.

- [ ] **Track D: Data warm-up**
  - Solve tiny CSV/JSON cleanup tasks before heavier ML work.

---

# Progress Log

## Current status
- **Current phase:** Phase 0 — Orientation + Core Syntax
- **Current lecture:** L03
- **Last completed lecture:** L02
- **Overall status:** In progress

## Daily log
- **Day 1 (2026-03-12):** Completed L01 — Python basics for an AI learner. Covered operators, conditionals, truthiness/falsiness, `==` vs `is`, `None`, collections, common errors, copy-vs-reference, and beginner Python traps. Notes stored in `python-for-ai/lecture-1/notes-1.md`.
- **Day 2 (2026-03-13):** Completed L02 — Functions, lists, dicts, and debugging like a Pythonista. Covered `return` vs `print`, list and dict usage, `IndexError`/`KeyError`, debugging common assumptions, shared-reference bugs, and the mutable default argument trap. Notes stored in `python-for-ai/lecture-2/notes-2.md`.
- **Day 3:** _Pending_
- **Day 4:** _Pending_
- **Day 5:** _Pending_

---

# Notes for Future Updates

This roadmap is version 1.

We may later add:
- more hands-on mini projects
- dedicated NumPy/pandas exercises
- AI API integration exercises
- simple ML starter projects
- interview-style Python drills if useful

For now, the goal is simple:
**build strong Python foundations first, then connect them directly to AI work.**

---

# Rule for Daily Study

When continuing from this roadmap on any day:
1. resume from the **current lecture**
2. teach simply with small runnable examples
3. include at least one short exercise
4. save important notes after class
5. update roadmap progress after finishing
