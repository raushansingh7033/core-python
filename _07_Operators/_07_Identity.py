# Used to check if two variables refer to the same object (same memory location).

p = [1, 2, 3]
q = p       # q points to the same object as p
r = [1, 2, 3]  # r is a different object with same values

print("p is q:", p is q)       # True → both point to same object
print("p is r:", p is r)       # False → different objects
print("p is not r:", p is not r) # True → p and r are different
