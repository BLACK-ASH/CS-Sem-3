class Node:
    def __init__(self,c,v,e,nextNode=None):
        self.c = c
        self.v = v
        self.e = e
        self.nextNode = nextNode

class Polynomial:
    def __init__(self):
        self.head = None

    def print(self):
        curr = self.head
        equation = ""
        while curr:
            if curr.c > 0:
                equation += (f" + {curr.c}{curr.v}^{curr.e} ") 
            else:
                equation += (f" {curr.c}{curr.v}^{curr.e} ") 
            curr = curr.nextNode
        print(equation)
                
    def insert(self,c,v,e):
        curr = self.head
        if curr == None:
            newNode = Node(c,v,e,curr)
            self.head = newNode
            return True

        # If Coeffient Is Greater Than Head
        if e >= curr.e:
            # If Variable With Same Power Exist
            if curr.v == v and curr.e==e:
                curr.c +=c
                return True
                
            newNode = Node(c,v,e,curr)
            self.head = newNode
            return True
            
        # If Coeffient Is Smaller Than Head

        # 1. Finding Position
        while curr.nextNode:
            if e > curr.e:
                break
            curr = curr.nextNode

        # 2. Adding Node
         # If Variable With Same Power Exist
        if curr.v == v and curr.e==e:
            curr.c +=c
            return True
        
        newNode = Node(c,v,e,curr.nextNode)
        curr.nextNode = newNode
        return True

    def add(self,e):
        curr = e.head
        while curr:
            self.insert(curr.c,curr.v,curr.e)
            curr = curr.nextNode
        return True
            
        
# First Equation
p = Polynomial()
p.insert(2,"x",3)
p.insert(2,"x",4)
p.insert(2,"x",5)
p.print()

# Second Equation
e = Polynomial()
e.insert(2,"x",1)
e.insert(2,"x",1)
e.insert(3,"x",5)
e.print()

# Adding Equation
p.add(e)
p.print()
