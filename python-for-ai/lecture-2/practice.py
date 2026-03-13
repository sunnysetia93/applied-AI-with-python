def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet('Sunny'))

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item('apple'))
print(add_item('banana'))
# One-line rule
# Never use a mutable object like [], {}, or set() as a default function argument unless you intentionally want shared state.

# Easy mental model

# Bad version:

# • default list is created once
# • reused forever

# Good version:

# • None is the default
# • actual list is created per call


def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

print(add_tag('python'))
print(add_tag('ai'))
