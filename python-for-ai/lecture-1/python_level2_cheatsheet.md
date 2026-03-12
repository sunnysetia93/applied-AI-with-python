# Python Level 2 Cheat Sheet

A compact reference for common Python concepts, traps, and interview-style questions.

---

## 1) List vs Tuple vs Set vs Dict

### List
- Ordered
- Mutable
- Allows duplicates

```python
x = [1, 2, 2, 3]
```

Use when:
- you need ordering
- you may modify values

### Tuple
- Ordered
- Immutable
- Allows duplicates

```python
x = (1, 2, 2, 3)
```

Use when:
- data should not change
- you want fixed grouped values

### Set
- Unordered
- Mutable
- No duplicates

```python
x = {1, 2, 2, 3}
# {1, 2, 3}
```

Use when:
- uniqueness matters
- membership checks are important

### Dict
- Key-value mapping
- Mutable
- Keys must be unique

```python
x = {"name": "Sunny", "age": 25}
```

Use when:
- you want labeled data

---

## 2) Mutability

### Mutable objects
Can be changed after creation:
- list
- dict
- set

```python
x = [1, 2]
x.append(3)
print(x)  # [1, 2, 3]
```

### Immutable objects
Cannot be changed after creation:
- int
- float
- str
- tuple
- bool

```python
x = "hello"
# x[0] = "H"  -> error
```

Important:
Sometimes it looks like a value changed, but actually a new object was created.

```python
x = 5
x = x + 1
```

---

## 3) Assignment vs Copy

### Direct assignment
```python
a = [1, 2, 3]
b = a
```

Rule:
- `a` and `b` point to the same object

```python
b.append(4)
print(a)  # [1, 2, 3, 4]
```

### Shallow copy
```python
a = [1, 2, 3]
b = a[:]
```

Now `b` is a new list.

```python
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

Other common shallow copy forms:

```python
b = a.copy()
b = list(a)
```

---

## 4) Shallow Copy vs Deep Copy

### Shallow copy
Copies the outer object only.

```python
a = [[1, 2], [3, 4]]
b = a[:]
```

If you change an inner list:

```python
b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]]
```

Because inner lists are still shared.

### Deep copy
Copies everything recursively.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 2, 99], [3, 4]]
```

Rule:
- shallow copy = outer new, inner may still be shared
- deep copy = fully independent copy

---

## 5) `==` vs `is`

- `==` checks value equality
- `is` checks object identity

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Use `is` mainly for:
- `None`
- identity checks

Best practice:

```python
if x is None:
    ...
```

---

## 6) Truthy and Falsy

### Falsy values
- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`
- `()`

### Truthy values
Almost everything else.

Examples:

```python
bool("")    # False
bool(" ")   # True
bool([])    # False
bool([0])   # True
bool(0)     # False
bool(1)     # True
```

Important trap:

```python
if [0]:
    print("True")
```

This prints `True` because the list is non-empty.

---

## 7) Operator Precedence

Python follows precedence rules.

Common order:
1. `**`
2. unary `+`, `-`, `not`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. comparisons: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`
6. `not`
7. `and`
8. `or`

Example:

```python
print(2 + 3 * 4)  # 14
```

Use parentheses when in doubt:

```python
print((2 + 3) * 4)  # 20
```

---

## 8) `and` / `or` do not always return `True` / `False`

This is a classic trap.

```python
print(0 or 5)      # 5
print("" or "hi")  # hi
print(3 and 7)     # 7
print(0 and 7)     # 0
```

Rule:
- `or` returns the first truthy value, otherwise the last value
- `and` returns the first falsy value, otherwise the last value

Examples:

```python
x = "" or "Python"
print(x)  # Python

x = 5 and 10
print(x)  # 10
```

---

## 9) Chained Comparisons

```python
a < b < c
```

Means:

```python
a < b and b < c
```

Example:

```python
print(10 < 20 < 30)  # True
```

---

## 10) Booleans are integers underneath

In Python:

```python
True == 1    # True
False == 0   # True
```

Also:

```python
print(True + True + False)  # 2
```

Because:
- `True = 1`
- `False = 0`

---

## 11) Strings

### Strings are immutable
```python
x = "python"
# x[0] = "P" -> error
```

### Concatenation
```python
print("Py" + "thon")  # Python
```

### Repetition
```python
print("ha" * 3)  # hahaha
```

### Indexing
```python
x = "Python"
print(x[0])   # P
print(x[-1])  # n
```

### Slicing
```python
x = "Python"
print(x[0:2])  # Py
print(x[:4])   # Pyth
print(x[::2])  # Pto
```

---

## 12) Lists

### Common operations
```python
x = [1, 2, 3]
x.append(4)
x.pop()
x.insert(1, 99)
x.remove(2)
```

### Slicing
```python
x = [10, 20, 30, 40]
print(x[1:3])  # [20, 30]
```

### Membership
```python
print(20 in x)  # True
```

---

## 13) Tuples

Tuples are immutable.

```python
x = (1, 2, 3)
print(x[1])  # 2
```

Single-element tuple needs a comma:

```python
x = (5,)
```

Without comma:

```python
x = (5)
```

This is just an integer.

---

## 14) Sets

Rules:
- no duplicates
- unordered
- cannot access by index

```python
x = {1, 2, 2, 3}
print(x)  # {1, 2, 3}
```

Useful operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
```

---

## 15) Dictionaries

### Access values
```python
x = {"a": 1, "b": 2}
print(x["a"])  # 1
```

### Missing key
```python
print(x["c"])  # KeyError
```

Safer:

```python
print(x.get("c"))      # None
print(x.get("c", 0))   # 0
```

### Add or update
```python
x["c"] = 3
```

### Iterate
```python
for key, value in x.items():
    print(key, value)
```

---

## 16) Common Errors

### `TypeError`
Wrong operation for a type.

```python
"10" + 5  # TypeError
```

### `IndexError`
Index out of range.

```python
x = []
x[0]  # IndexError
```

### `KeyError`
Missing dictionary key.

```python
x = {"a": 1}
x["b"]  # KeyError
```

### `ValueError`
Correct type, wrong value.

```python
int("abc")  # ValueError
```

### `NameError`
Variable not defined.

```python
print(age)  # NameError
```

---

## 17) `None` Rules

`None` means absence of value.

```python
x = None
```

Best check:

```python
if x is None:
    ...
```

Important:
- `None == False` is `False`
- `None is False` is `False`

---

## 18) Function Argument Mutability Trap

Mutable defaults are dangerous.

Bad:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

This list is reused across calls.

Better:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 19) Looping Tips

### Over a list
```python
for x in [1, 2, 3]:
    print(x)
```

### With index
```python
for i, x in enumerate(["a", "b", "c"]):
    print(i, x)
```

### Over a dict
```python
d = {"a": 1, "b": 2}

for k in d:
    print(k)

for k, v in d.items():
    print(k, v)
```

---

## 20) Membership Rules

```python
2 in [1, 2, 3]           # True
"a" in "cat"            # True
"x" in {"x": 1, "y": 2}  # True
```

Important:
For dicts, `in` checks keys, not values.

```python
1 in {"x": 1, "y": 2}  # False
```

---

## 21) Unpacking

```python
a, b = 1, 2
print(a, b)  # 1 2
```

```python
x = [10, 20, 30]
a, b, c = x
```

Extended unpacking:

```python
a, *middle, c = [1, 2, 3, 4, 5]
print(a)       # 1
print(middle)  # [2, 3, 4]
print(c)       # 5
```

---

## 22) Useful Built-ins

### `type()`
```python
print(type(5))      # <class 'int'>
print(type("hi"))   # <class 'str'>
```

### `len()`
```python
len([1, 2, 3])  # 3
```

### `sum()`
```python
sum([1, 2, 3])  # 6
```

### `max()` / `min()`
```python
max([1, 7, 2])  # 7
min([1, 7, 2])  # 1
```

### `sorted()`
```python
sorted([3, 1, 2])  # [1, 2, 3]
```

---

## 23) Interview-Style Python Traps

### Trap 1: shared reference
```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

### Trap 2: shallow copy of nested list
```python
a = [[1], [2]]
b = a[:]
b[0].append(99)
print(a)  # [[1, 99], [2]]
```

### Trap 3: bool/int confusion
```python
print(True == 1)  # True
```

### Trap 4: empty vs non-empty
```python
print(bool([0]))  # True
```

### Trap 5: string vs int
```python
print("10" == 10)  # False
```

### Trap 6: `is` vs `==`
```python
a = [1]
b = [1]

print(a == b)  # True
print(a is b)  # False
```

### Trap 7: missing dict key
```python
d = {"a": 1}
print(d["b"])  # KeyError
```

---

## 24) Fast Exam Strategy for Output Questions

When you see a Python code question, check in this order:

1. Identify the type
   - int?
   - string?
   - list?
   - tuple?
   - set?
   - dict?
   - `None`?
2. Check truthiness
3. Watch for mutability
   - did code modify original object?
   - was it copied or referenced?
4. Check `==` vs `is`
   - value equality?
   - same object?
5. Check for error
   - missing key?
   - invalid index?
   - wrong type operation?
6. Check precedence
   - multiplication before addition?
   - `not`, `and`, `or`?

---

## 25) Super-Short Summary

- list = ordered, mutable
- tuple = ordered, immutable
- set = unique values, unordered
- dict = key-value pairs
- `==` checks value
- `is` checks identity
- empty containers are falsy
- non-empty containers are truthy
- `"10"` is not `10`
- `True == 1`, `False == 0`
- `y = x` shares object
- `x[:]` makes a shallow copy
- nested lists need deep copy if full independence is required
- dict missing key -> `KeyError`

---

## 26) Practice Questions

### Q1
```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

### Q2
```python
a = [1, 2]
b = a[:]
b.append(3)
print(a, b)
```

### Q3
```python
print(bool(""), bool(" "), bool([]), bool([0]))
```

### Q4
```python
a = [1]
b = [1]
print(a == b, a is b)
```

### Q5
```python
d = {"x": 10}
print(d.get("y", 0))
```

### Q6
```python
print(2 + 3 * 4)
```

### Q7
```python
print((2 + 3) * 4)
```

### Q8
```python
print(True + False + True)
```

### Answers
- Q1 -> `[1, 2, 3]`
- Q2 -> `[1, 2] [1, 2, 3]`
- Q3 -> `False True False True`
- Q4 -> `True False`
- Q5 -> `0`
- Q6 -> `14`
- Q7 -> `20`
- Q8 -> `2`
