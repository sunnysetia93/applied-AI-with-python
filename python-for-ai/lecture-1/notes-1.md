# Lecture 1 Notes

A cleaned summary of the first Python for AI lecture.

---

## Python libraries commonly used in AI

- **NumPy** → fast numerical operations and arrays
- **pandas** → working with tabular data
- **matplotlib** → charts and visualizations
- **scikit-learn** → classical machine learning
- **PyTorch / TensorFlow** → deep learning

---

## Core arithmetic operators

```python
print(10 % 3)   # 1   -> modulus (remainder)
print(2 ** 3)   # 8   -> power
print(10 // 3)  # 3   -> floor division
```

### Quick meaning
- `%` gives the remainder
- `**` raises to a power
- `//` divides and keeps only the whole-number part

---

## Conditionals

Python uses `if`, `elif`, and `else` to make decisions.

```python
x = 7

if x < 5:
    print("A")
elif x < 10:
    print("B")
else:
    print("C")
```

### Logical operators
Used to combine conditions:
- `and`
- `or`
- `not`

Example:

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

---

## Python Rules Cheat Sheet

### 1) Truthy and falsy values

In `if` conditions, Python checks whether a value is truthy or falsy.

#### Falsy values
These behave like `False`:
- `False`
- `None`
- `0`
- `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `set()` (empty set)
- `()` (empty tuple)

#### Truthy values
Almost everything else is truthy:
- non-zero numbers like `5`, `-1`
- non-empty strings like `"hi"` or even `" "`
- non-empty lists like `[0]`
- non-empty dicts like `{"a": 1}`

Examples:

```python
if 5:      # True
if 0:      # False
if " ":    # True
if "":     # False
if []:     # False
if [0]:    # True
```

---

### 2) `if`, `elif`, `else`

Python evaluates conditions from top to bottom.

```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

- If `condition1` is true, Python stops there.
- `elif` runs only if earlier conditions fail.
- `else` runs if nothing matched.

---

### 3) Comparison operators

- `==` value equality
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

Example:

```python
x = 10
print(x == 10)  # True
print(x != 5)   # True
print(x > 3)    # True
```

---

### 4) Logical operators

#### `and`
Both conditions must be true.

```python
True and True   # True
True and False  # False
```

#### `or`
At least one condition must be true.

```python
True or False   # True
False or False  # False
```

#### `not`
Reverses the truth value.

```python
not True   # False
not False  # True
```

---

### 5) Chained comparisons

Python allows this:

```python
a < b < c
```

It means:

```python
a < b and b < c
```

Example:

```python
10 < 20 < 30  # True
```

---

### 6) Strings vs integers

A string and a number are different.

```python
"10"  # string
10    # integer
```

So:

```python
"10" == 10    # False
"10" == "10"  # True
```

Rule:
- quotes = string
- no quotes = number / variable / object

---

### 7) `bool()` conversion rules

`bool(value)` converts a value to `True` or `False`.

```python
bool("")    # False
bool(" ")   # True
bool(0)     # False
bool(1)     # True
bool([])    # False
bool([0])   # True
```

---

### 8) `True` and `False` are special numbers in Python

Python treats:
- `True` as `1`
- `False` as `0`

```python
True + True + False  # 2
```

Also:

```python
1 == True   # True
0 == False  # True
```

This is valid Python, but it can be confusing.

---

### 9) `==` vs `is`

- `==` checks whether values are equal
- `is` checks whether two variables point to the same object in memory

```python
a = []
b = []

print(a == b)  # True
print(a is b)  # False
```

Example with aliasing:

```python
x = [1, 2]
y = x

print(x is y)  # True
```

---

### 10) `None`

`None` means “no value” or “nothing”.

Best practice:

```python
x = None
print(x is None)   # True
print(x == False)  # False
print(x is False)  # False
```

Rule:
- `None` is not the same as `False`
- `None` is its own special singleton object

---

### 11) Empty vs non-empty collections

Collections:
- list `[]`
- tuple `()`
- dict `{}`
- set `set()`

Rule:
- empty collection = falsy
- non-empty collection = truthy

```python
if []:        # False
if [0]:       # True
if {}:        # False
if {"a": 1}:  # True
```

Important: `[0]` is truthy because the list is non-empty, even though `0` is falsy.

---

### 12) Short-circuit logic

Python may stop early in logical expressions.

- In `and`, if the first part is false, Python may not check the rest.
- In `or`, if the first part is true, Python may not check the rest.

```python
x = [0]
if x and x[0]:
    print("A")
else:
    print("B")
```

Why this is safe:
- first `x` checks whether the list is non-empty
- only then `x[0]` is evaluated

---

### 13) List copying vs reference sharing

#### Same object

```python
x = [1, 2]
y = x

y.append(3)
print(x)  # [1, 2, 3]
```

#### Shallow copy

```python
x = [1, 2, 3]
y = x[:]

y.append(4)
print(x)  # [1, 2, 3]
print(y)  # [1, 2, 3, 4]
```

Rule:
- `y = x` → same list
- `y = x[:]` → copy of the list

---

### 14) `len()`

`len()` gives the number of items.

```python
len([1, 2, 3])  # 3
len("")         # 0
len("Python")   # 6
```

---

### 15) Tuples

A tuple is like a list, but immutable.

```python
x = (1, 2, 3)
print(x[1])  # 2
```

Indexing starts from `0`.

---

### 16) Sets

A set stores unique values only.

```python
x = {1, 2, 2, 3}
print(x)  # {1, 2, 3}
```

Rule:
- duplicates are removed automatically
- sets are unordered, so printed order may vary

---

### 17) Dictionaries

A dictionary stores key-value pairs.

```python
x = {"a": 1, "b": 2}
print(x["a"])  # 1
```

If a key does not exist:

```python
print(x["c"])  # KeyError
```

Safer option:

```python
print(x.get("c"))     # None
print(x.get("c", 0))  # 0
```

---

### 18) Common error types

```python
x = {"a": 1}
x["b"]          # KeyError

x = []
x[0]             # IndexError

"10" + 5         # TypeError
int("abc")       # ValueError
print(age)        # NameError
```

---

## Fast mental checklist for output questions

When you see a code question, check in this order:

1. What is the type?
   - string?
   - int?
   - bool?
   - list?
   - dict?
   - `None`?
2. Is it truthy or falsy?
3. Is it checking value or identity?
   - `==` → value
   - `is` → same object
4. Is it same reference or copy?
   - `y = x` → same object
   - `y = x[:]` → copy
5. Could it raise an error?
   - missing dict key?
   - bad index?
   - invalid type operation?

---

## Biggest traps from Lecture 1

- Empty containers are falsy
- Non-empty containers are truthy
- `"10"` is not `10`
- `==` is not `is`
- `None` is not `False`
- `True == 1` and `False == 0`
- `y = x` shares the same list
- sets remove duplicates
- missing dict key gives `KeyError`
