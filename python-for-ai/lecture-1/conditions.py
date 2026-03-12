"""Lecture 1 examples: conditionals, copying, and deep copy."""

import copy

print("=== Chained comparison ===")
a = 10
b = 20
c = 30

if a < b < c:
    print("X")
else:
    print("Y")

print("\n=== Shallow copy with nested lists ===")
original = [[1, 2], [3, 4]]
shallow_copy = original[:]
shallow_copy[0].append(99)

print("original:", original)        # inner list is shared
print("shallow_copy:", shallow_copy)

print("\n=== Deep copy with nested lists ===")
original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)
deep_copy[0].append(99)

print("original:", original)        # unchanged
print("deep_copy:", deep_copy)
