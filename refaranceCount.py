import sys

a = [1, 2, 3]

print(sys.getrefcount(a))  

b = a
print(sys.getrefcount(a))  # Outputs 3

c = a
print(sys.getrefcount(a))  # Outputs 4

del b
print(sys.getrefcount(a))  # Outputs 3

del c
print(sys.getrefcount(a))  # Outputs 2

del a
