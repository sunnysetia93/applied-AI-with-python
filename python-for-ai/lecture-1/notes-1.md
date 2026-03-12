• NumPy → math with arrays
• pandas → working with data
• matplotlib → charts
• scikit-learn → machine learning
• PyTorch / TensorFlow → deep learning

% modulus → remainder
** power
// floor division
print(10 % 3) # 1
print(2 ** 3) # 8
print(10 // 3) # 3

Logical operators
Used to combine conditions:

• and
• or
• not


Good call. Here’s the rule sheet / cheat sheet for the questions we covered.

Python Rules Cheat Sheet

1) Truthy and falsy values

In if conditions, Python checks whether a value is truthy or falsy.

Falsy values

These behave like False:

• False
• None
• 0
• 0.0
• "" empty string
• [] empty list
• {} empty dict
• set() empty set
• () empty tuple

Truthy values

Almost everything else is truthy:

• non-zero numbers like 5, -1
• non-empty strings like "hi" or even " " (space)
• non-empty lists like [0]
• non-empty dicts like {"a": 1}

Examples

if 5: # True
if 0: # False
if " ": # True
if "": # False
if []: # False
if [0]: # True

───

2) if, elif, else

Python evaluates conditions from top to bottom.

if condition1:
...
elif condition2:
...
else:
...

• If condition1 is true, Python stops there
• elif runs only if earlier conditions fail
• else runs if nothing matched

───

3) Comparison operators

• == value equality
• != not equal
• > greater than
• < less than
• >= greater than or equal
• <= less than or equal

Example

x = 10
x == 10 # True
x != 5 # True
x > 3 # True

───

4) Logical operators

and

Both conditions must be true.

True and True # True
True and False # False

or

At least one condition must be true.

True or False # True
False or False # False

not

Reverses truth value.

not True # False
not False # True

Example

if age >= 18 and has_id:
print("Allowed")

───

5) Chained comparisons

Python allows this:

a < b < c

It means:

a < b and b < c

Example

10 < 20 < 30 # True

───

6) Strings vs integers

A string and a number are different.

"10" # string
10 # integer

So:

"10" == 10 # False
"10" == "10" # True

Rule:

• Quotes = string
• No quotes = number / variable / other object

───

7) bool() conversion rules

bool(value) converts any value to True or False.

Examples

bool("") # False
bool(" ") # True
bool(0) # False
bool(1) # True
bool([]) # False
bool([0]) # True

───

8) True and False are special numbers in Python

Python treats:

• True as 1
• False


Good call. Here’s the rule sheet / cheat sheet for the questions we covered.

Python Rules Cheat Sheet

1) Truthy and falsy values

In if conditions, Python checks whether a value is truthy or falsy.

Falsy values

These behave like False:

• False
• None
• 0
• 0.0
• "" empty string
• [] empty list
• {} empty dict
• set() empty set
• () empty tuple

Truthy values

Almost everything else is truthy:

• non-zero numbers like 5, -1
• non-empty strings like "hi" or even " " (space)
• non-empty lists like [0]
• non-empty dicts like {"a": 1}

Examples

if 5: # True
if 0: # False
if " ": # True
if "": # False
if []: # False
if [0]: # True

───

2) if, elif, else

Python evaluates conditions from top to bottom.

if condition1:
...
elif condition2:
...
else:
...

• If condition1 is true, Python stops there
• elif runs only if earlier conditions fail
• else runs if nothing matched

───

3) Comparison operators

• == value equality
• != not equal
• > greater than
• < less than
• >= greater than or equal
• <= less than or equal

Example

x = 10
x == 10 # True
x != 5 # True
x > 3 # True

───

4) Logical operators

and

Both conditions must be true.

True and True # True
True and False # False

or

At least one condition must be true.

True or False # True
False or False # False

not

Reverses truth value.

not True # False
not False # True

Example

if age >= 18 and has_id:
print("Allowed")

───

5) Chained comparisons

Python allows this:

a < b < c

It means:

a < b and b < c

Example

10 < 20 < 30 # True

───

6) Strings vs integers

A string and a number are different.

"10" # string
10 # integer

So:

"10" == 10 # False
"10" == "10" # True

Rule:

• Quotes = string
• No quotes = number / variable / other object

───

7) bool() conversion rules

bool(value) converts any value to True or False.

Examples

bool("") # False
bool(" ") # True
bool(0) # False
bool(1) # True
bool([]) # False
bool([0]) # True

───

8) True and False are special numbers in Python

Python treats:

• True as 1
• False as 0

So:

True + True + False
# 1 + 1 + 0 = 2

Also:

1 == True # True
0 == False # True

But be careful:
this is allowed, but not always good style.

───

9) == vs is

This is a very important rule.

==

Checks whether values are equal

is

Checks whether two variables point to the same object in memory

Example

a = []
b = []

a == b # True (same contents)
a is b # False (different objects)

Example with aliasing

x = [1, 2]
y = x

Now:

x is y # True

Because both point to the exact same list.

───

10) None

None means “no value” / “nothing”.

Best practice

Check it with is None, not == None

x = None

x is None # True
x == False # False
x is False # False

Rule

• None is not the same as False
• None is its own special singleton object

───

11) Empty vs non-empty collections

Collections:

• list []
• tuple ()
• dict {}
•

set set()

Rule:

• empty collection = falsy
• non-empty collection = truthy

Examples

if []: # False
if [0]: # True
if {}: # False
if {"a":1}: # True

Important:

[0]

is truthy because the list is non-empty, even though 0 itself is falsy.

───

12) Short-circuit logic

Python may stop early in logical expressions.

and

If first part is false, Python may not check the rest.

or

If first part is true, Python may not check the rest.

Example:

x = [0]
if x and x[0]:
print("A")
else:
print("B")

Why this is safe:

• first x checks if list is non-empty
• only then x[0] is evaluated

This prevents index errors in many real cases.

───

13) List copying vs reference sharing

Same object

x = [1, 2]
y = x

Now both point to same list.
If you change one, the other changes too.

y.append(3)
print(x) # [1, 2, 3]

Shallow copy

x = [1, 2, 3]
y = x[:]

Now y is a new list with same elements.

y.append(4)
print(x) # [1, 2, 3]
print(y) # [1, 2, 3, 4]

Rule:

• y = x → same list
• y = x[:] → copy of list

───

14) len()

len() gives the number of items.

len([1, 2, 3]) # 3
len("") # 0
len("Python") # 6

───

15) Tuples
A tuple is like a list, but immutable.

x = (1, 2, 3)
print(x[1]) # 2

Indexing starts from 0:

• x[0] → 1
• x[1] → 2
• x[2] → 3

───

16) Sets

A set stores unique values only.

x = {1, 2, 2, 3}
print(x)

Output becomes something like:

{1, 2, 3}

Rule:

• duplicates are automatically removed
• sets are unordered, so display order may vary

So don’t rely on exact printed order.

───

17) Dictionaries

A dict stores key-value pairs.

x = {"a": 1, "b": 2}
print(x["a"]) # 1

Important rule

If key does not exist:

print(x["c"])

Python raises:

KeyError

So missing keys cause an error unless you use safer methods like get().

───

18) Common error types from these examples

KeyError

When dictionary key is missing.

x = {"a": 1}
x["b"] # KeyError

IndexError

When list index does not exist.

x = []
x[0] # IndexError

TypeError

When operation is not valid for given types.

"10" + 5 # TypeError

───

Fast mental rules for code prediction

When you see a question, check in this order:

A. What is the type?

• string?
• int?
• bool?
• list?
• dict?
• None?

B. Is it truthy or falsy?

Especially in if.

C. Is it checking value or identity?

• == → value
• is → same object

D. Is it same reference or copy?

• y = x → same object
• y = x[:] → copy

E. Could it raise an error?

• missing dict key?
• bad index?
• invalid type operation?

───

One-line summary of the biggest traps

• Empty containers are falsy
• Non-empty containers are truthy
• "10" is not 10
• == is not is
• None is not False
• True == 1 and False == 0
• y = x shares the same list
• sets remove duplicates
• missing dict key gives KeyError

───

If you want, next I can make you a Level 2 sheet covering:

• list vs tuple vs set vs dict
• mutability
• shallow vs deep copy
• operator precedence
• common interview-style Python traps

That would be a very useful save-worthy reference.