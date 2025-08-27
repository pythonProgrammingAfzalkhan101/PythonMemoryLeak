class A:
    def __init__(self):
        self.b  = None 

class B:
    def __init__(self):
        self.a = None  

a = A()
b = B()

a.b  = b 
b.a = a 

del a 
del b 
