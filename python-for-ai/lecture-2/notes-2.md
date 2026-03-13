# Lecture 2 — Functions, Lists, Dicts, and Debugging Like a Pythonista

**Date:** 2026-03-13  
**Status:** Done  
**Roadmap lecture:** L02 — Functions, lists, dicts, and debugging like a Pythonista

---

## Objective
Build early Python instincts around writing small functions, using lists and dicts correctly, debugging common beginner errors, and avoiding awkward “JS written in Python” habits.

---

## Core Concepts Covered

### 1) Functions should usually return values
A major beginner trap is using `print()` where `return` is needed.

Bad:

```python
def add(a, b):
    print(a + b)
```

Better:

```python
def add(a, b):
    return a + b
```

Key idea:
- `print()` displays a value
- `return` sends a value back to the caller
- if a function does not explicitly return, Python returns `None`

Example:

```python
def square(x):
    print(x * x)

result = square(4)
print(result)
```

Output:

```python
16
None
```

---

### 2) Default arguments and the mutable-default trap
Covered the classic Python trap:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Why it behaves strangely:
- the default list is created once at function definition time
- each call without an explicit `items` argument reuses that same list object
- the parameter name is local to each call, but it points to the same shared object

Safe version:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

Student follow-up question captured:
- Asked why the list is reused if parameters are scoped to the function.
- Clarified that the parameter variable is local, but the default object itself is created once and reused across calls.

---

### 3) Lists
Reviewed lists as:
- ordered
- mutable
- duplicate-friendly

Common operations discussed:

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.remove("banana")
```

Also covered:
- indexing
- negative indexing
- slicing

Examples:

```python
nums = [10, 20, 30]
print(nums[0])   # 10
print(nums[-1])  # 30
print(nums[0:2]) # [10, 20]
```

---

### 4) Common list mistakes
#### `IndexError`

```python
x = []
print(x[0])
```

This fails because the list is empty.

Safer pattern:

```python
if x:
    print(x[0])
```

#### Shared reference bug

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

Reason:
- `b = a` does not copy the list
- both variables refer to the same object

Safer copy patterns:

```python
b = a[:]
# or
b = a.copy()
```

---

### 5) Dicts
Reviewed dictionaries as key-value mappings.

Example:

```python
user = {
    "name": "Sunny",
    "role": "student",
    "age": 25
}
```

Covered:
- lookup by key
- update by key
- adding new key-value pairs

Examples:

```python
print(user["name"])
user["age"] = 26
user["city"] = "Delhi"
```

---

### 6) Common dict mistakes
#### `KeyError`

```python
user = {"name": "Sunny"}
print(user["age"])
```

Safer approach:

```python
user.get("age")
user.get("age", 0)
```

Key idea:
- direct lookup with `[]` assumes the key exists
- `.get()` is safer when the key may be missing

---

### 7) JS brain vs Python brain
Discussed how JavaScript habits can make early Python code noisy or awkward.

Pythonic direction:
- smaller functions
- clearer naming
- use truthy/falsy naturally
- use built-ins and dict methods instead of verbose manual logic
- prioritize readability over ceremony

Example shown:

Less Pythonic:

```python
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
```

Better:

```python
def is_even(x):
    return x % 2 == 0
```

---

### 8) Common beginner error types reviewed
- `TypeError` — wrong operation for a type
- `IndexError` — list index out of range
- `KeyError` — missing dictionary key
- `NameError` — variable not defined
- `ValueError` — right type, wrong value

Examples used:

```python
"10" + 5        # TypeError
[].__getitem__(0) # conceptually IndexError via x[0]
{"a": 1}["b"]   # KeyError
print(age)       # NameError
int("abc")      # ValueError
```

---

## Debugging Framework Taught
When code breaks, check in this order:

1. What is the type?
2. What is the actual value?
3. Which line failed?
4. What assumption was wrong?

Typical wrong assumptions:
- assumed list has an item
- assumed dict key exists
- assumed string is numeric
- assumed a function returned a value when it only printed

---

## Exercise Review
### Prompted questions
1. `multiply(3, 4)` -> `12`
2. `greet()` bug -> prints but does not return, so assigned result is `None`
3. `data[0]` on empty list -> `IndexError`
4. `user["age"]` when missing -> `KeyError`
5. `def add_tag(tag, tags=[]): ...` behaves strangely because the default list is created once and reused across calls; fix by using `None` and creating a new list inside the function

### Student answers
Student got all 5 essentially correct.

Notable strong answer:
- correctly explained the mutable-default trap and the `None` fix

---

## Key Takeaways
- prefer `return` over `print` when the caller needs the result
- lists are mutable and index-based
- dicts are key-based and may raise `KeyError` when keys are missing
- `b = a` shares the same list object rather than copying it
- default mutable arguments are created once and can leak state across calls
- many debugging problems come from incorrect assumptions about data shape or function behavior
- cleaner Python is usually shorter and less ceremonial than JS-style Python

---

## One-Line Summary
**Write small functions that return values, treat lists and dicts carefully, and debug by checking types, values, and broken assumptions before guessing.**

---

## Status Update for Next Session
- **Completed today:** L02 — Functions, lists, dicts, and debugging like a Pythonista
- **Next recommended lecture:** L03 — Strings, slicing, and everyday built-ins
- **Next class plan:** build comfort with strings, slicing, membership checks, and high-value built-ins used constantly in Python
