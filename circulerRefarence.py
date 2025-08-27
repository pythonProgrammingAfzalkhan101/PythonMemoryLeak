import weakref

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = Node 

node1 = Node(1)
node2 = Node(2)

node1.next = weakref.ref(node2)
node2.next = weakref(node1)

