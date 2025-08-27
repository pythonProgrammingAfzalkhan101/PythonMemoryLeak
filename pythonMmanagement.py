import sys 

a = [1 ,2, 3,4]
b = a 
c = a

print("Memory Count refarance:")
print("refcount(a):",sys.getrefcount(a))
print("refcount(b):",sys.getrefcount(b))
print("refcount(c):",sys.getrefcount(c))

print("\nDelete reference 'a'")

try:
    del a  
    print("Deleted a Successfully")
    print("refcount(b):",sys.getrefcount(b))
    print("refcount(c):",sys.getrefcount(c))

except Exception as e:
    print("Error:",e)

print("\nDelete reference 'b'")
try:
    del b
    print("Deleted b Successfully")
    print("refcount(b)",sys.getrefcount(c))
except Exception as e:
    print("Error",e)
try:
    del c 
    print("Deleted c Successfully")
except Exception as e:
    print("Error",e)
