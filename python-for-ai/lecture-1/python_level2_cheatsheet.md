Yep — here’s a clean Markdown note you can save as something like python_level2_cheatsheet.md.

# Python Level 2 Cheat Sheet

A compact reference for common Python concepts, traps, and interview-style questions.

---

# 1) List vs Tuple vs Set vs Dict

## List
- Ordered
- Mutable
- Allows duplicates

```python
x = [1, 2, 2, 3]

Use when:

• you need ordering
• you may modify values

───

Tuple

• Ordered
• Immutable
• Allows duplicates

x = (1, 2, 2, 3)

Use when:

• data should not change
• you want fixed grouped values

───

Set

• Unordered
• Mutable
• No duplicates

x = {1, 2, 2, 3}
# {1, 2, 3}

Use when:

• uniqueness matters
• membership checks are important

───

Dict

• Key-value mapping
• Mutable
• Keys must be unique

x = {"name": "Sunny", "age": 25}

Use when:

• you want labeled data

───

2) Mutability

Mutable objects

Can be changed after creation:

• list
• dict
• set

x = [1, 2]
x.append(3)
print(x) # [1, 2, 3]

───

Immutable objects

Cannot be changed after creation:

• int
• float
• str
• tuple
• bool

x = "hello"
# x[0] = "H" -> error

Important:
Sometimes it looks like a value changed, but actually a new object was created.

x = 5
x = x + 1

This does not modify the old integer. It creates a new one.

───

3) Assignment vs Copy

Direct assignment

a = [1, 2, 3]
b = a

Rule:

• a and b point to the same object

b.append(4)
print(a) # [1, 2, 3, 4]

───

Shallow copy

a = [1, 2, 3]
b = a[:]

Now b is a new list.

b.append(4)
print(a) # [1, 2, 3]
print(b) # [1, 2, 3, 4]

Other common shallow copy forms:

b = a.copy()
b = list(a)

───

4) Shallow Copy vs Deep Copy

Shallow copy

Copies outer object only.

a = [[1, 2], [3, 4]]
b = a[:]

If you change an inner list:

b[0].append(99)
print(a) # [[1, 2, 99], [3, 4]]

Because inner lists are still shared.

───

Deep copy

Copies everything recursively.

import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print(a) # [[1, 2], [3, 4]]
print(b) # [[1, 2, 99], [3, 4]]

Rule:

• shallow copy = outer new, inner may still be shared
• deep copy = fully independent copy

───

5) == vs is

==

Checks value equality

is

Checks object identity

a = [1, 2]
b = [1, 2]

print(a == b) # True
print(a is b) # False

Use is mainly for:

• None
• identity checks

Best practice:

if x is None:
...

Not:

if x == None:
...

───

6) Truthy and Falsy

Falsy values

• False
• None
• 0
• 0.0
• ""
• []
• {}
• set()
• ()

Truthy values

Almost everything else.

Examples:

bool("") # False
bool(" ") # True
bool([]) # False
bool([0]) # True
bool(0) # False
bool(1) # True

Important trap:

if [0]:
print("True")

This prints True because the list is non-empty.

───

7) Operator Precedence

Python follows precedence rules 
ens first.

Use parentheses when in doubt:

print((2 + 3) * 4) # 20

───

8) and / or do not always return True/False

This is a classic trap.

print(0 or 5) # 5
print("" or "hi") # hi
print(3 and 7) # 7
print(0 and 7) # 0

Rule:

• or returns the first truthy value, otherwise the last value
• and returns the first falsy value, otherwise the last value

Examples:

x = "" or "Python"
print(x) # Python

x = 5 and 10
print(x) # 10

───

9) Chained Comparisons

a < b < c

Means:

a < b and b < c

Example:

print(10 < 20 < 30) # True

───

10) Booleans are integers underneath

In Python:

True == 1 # True
False == 0 # True

Also:

print(True + True + False) # 2

Because:

• True = 1
• False = 0

This is valid Python, but can be confusing.

───

11) Strings

Strings are immutable

x = "python"
# x[0] = "P" -> error

Concatenation

print("Py" + "thon") # Python

Repetition

print("ha" * 3) # hahaha

Indexing

x = "Python"
print(x[0]) # P
print(x[-1]) # n

Slicing

x = "Python"
print(x[0:2]) # Py
print(x[:4]) # Pyth
print(x[::2]) # Pto

───

12) Lists

Common operations

x = [1, 2, 3]

x.append(4)
x.pop()
x.insert(1, 99)
x.remove(2)

Slicing

x = [10, 20, 30, 40]
print(x[1:3]) # [20, 30]

Membership

print(20 in x) # True

───

13) Tuples

Tuples are immutable.

x = (1, 2, 3)
print(x[1]) # 2

Single-element tuple needs a comma:

x = (5,)

Without comma:

x = (5)

This is just an integer.

───

14) Sets

Rules

• no duplicates
• unordered
• cannot access by index

x = {1, 2, 2, 3}
print(x) # {1, 2, 3}

Useful operations:

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # union
print(a & b) # intersection
print(a - b) # difference

───

15) Dictionaries

Access values

x = {"a": 1, "b": 2}
print(x["a"]) # 1

Missing key

print(x["c"]) # KeyError

Safer:

print(x.get("c")) # None
print(x.get("c", 0)) # 0

Add or update

x["c"] = 3

Iterate

for key, value in x.items():
print(key, value)

───

16) Common Errors

TypeError

Wrong operation for a type

"10" + 5 # TypeError

───

IndexError

Index out of range

x = []
x[0] # IndexError

───

KeyError

Missing dictionary key

x = {"a": 1}
x["b"] # KeyError

───

ValueError

Correct type, wrong value

int("abc") # ValueError

───

NameError

Variable not defined

print(age) # NameError

───

17) None Rules

None means absence of value.

x = None

Best check:

if x is None:
...

Important:

• None == False is False
• None is False is False

───

18) Function Argument Mutability Trap

Mutable defaults are dangerous.

Bad:

def add_item(item, items=[]):
items.append(item)
return items

This list is reused across calls.

Better:

def add_item(item, items=None):
if items is None:
items = []
items.append(item)
return items

This is a very common interview trap.

───

19) Looping Tips

Over list

for x in [1, 2, 3]:
print(x)

With index

for i, x in enumerate(["a", "b", "c"]):
print(i, x)

Over dict

d = {"a": 1, "b": 2}

for k in d:
print(k)

for k, v in d.items():
print(k, v)

───

20) Membership Rules

2 in [1, 2, 3] # True
"a" in "cat" # True
"x" in {"x": 1, "y": 2} # True

Important:
For dicts, in checks keys, not values.

1 in {"x": 1, "y": 2} # False

───

21) Unpacking

a, b = 1, 2
print(a, b) # 1 2

x = [10, 20, 30]
a, b, c = x

Extended unpacking:

a, *middle, c = [1, 2, 3, 4, 5]
print(a) # 1
print(middle) # [2, 3, 4]
print(c) # 5

───

22) Useful Built-ins

type()

print(type(5)) # <class 'int'>
print(type("hi")) # <class 'str'>

len()

len([1, 2, 3]) # 3

sum()

sum([1, 2, 3]) # 6

max() / min()

max([1, 7, 2]) # 7
min([1, 7, 2]) # 1

sorted()

sorted([3, 1, 2]) # [1, 2, 3]

───

23) Interview-Style Python Traps

Trap 1: shared reference

a = [1, 2]
b = a
b.append(3)
print(a) # [1, 2, 3]

Trap 2: shallow copy nested list

a = [[1], [2]]
b = a[:]
b[0].append(99)
print(a) # [[1, 99], [2]]

Trap 3: bool/int confusion

print(True == 1) # True

Trap 4: empty vs non-empty

print(bool([0]))

 # True

Trap 5: string vs int

print("10" == 10) # False

Trap 6: is vs ==

a = [1]
b = [1]

print(a == b) # True
print(a

is b) # False

Trap 7: missing dict key

d = {"a": 1}
print(d["b"]) # KeyError

───

24) Fast Exam Strategy for Output Questions

When you see a Python code question, check in this order:

Step 1: Identify the type

• int?
• string?
• list?
• tuple?
• set?
• dict?
• None?

Step 2: Check truthiness

Especially in if conditions.

Step 3: Watch for mutability

• did code modify original object?
• was it copied or referenced?

Step 4: Check == vs is

• value equality?
• same object?

Step 5: Check for error

• missing key?
• invalid index?
• wrong type operation?

Step 6: Check precedence

• multiplication before addition?
• not, and, or?

───

25) Super-Short Summary

• list = ordered, mutable
• tuple = ordered, immutable
• set = unique values, unordered
• dict = key-value pairs
• == checks value
• is checks identity
• empty containers are falsy
• non-empty containers are truthy
• "10" is not 10
• True == 1, False == 0
• y = x shares object
• x[:] makes shallow copy
• nested lists need deep copy if full independence is required
• dict missing key -> KeyError