# a = 10
# b = 20
# c = 30

# if a < b < c:
#     print("X")
# else:
#     print("Y")



# a = [[1, 2], [3, 4]]
# b = a[:]
# b[0].append(99)
# print(a) # [[1, 2, 99], [3, 4]]


import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print(a) # [[1, 2], [3, 4]]
print(b) # [[1, 2, 99], [3, 4]]