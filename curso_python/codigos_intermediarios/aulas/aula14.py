d1 = {
    'c1': 1,
    'c2': 2,

}

d2 = d1

d2['c1'] = 10

print(d1)

# shallow copy
d2 = d1.copy()

d2['c1'] = 1000

print(d1)
print(d2)


import copy

# deep cppy
d2 = copy.deepcopy(d1)

