class Stack:
    def __init__(self):
        self.data = []
        
    def isEmpty(self):
        return len(self.data)==0

    def peek(self):
        if not self.isEmpty(): 
            return self.data[-1]

    def push(self,e):
        self.data.append(e)

    def pop(self):
        return self.data.pop()

    def toString(self):
        return "".join(self.data)

class Delimeter:
    def __init__(self,exp):
        self.exp = exp

    def _match(self,a,b):
        if a == "{" and b =="}":
            return True
        elif a == "(" and b ==")":
            return True
        elif a == "[" and b =="]":
            return True
        else:
            return False

    def check(self):
        stack = Stack()
        for e in self.exp:
            if e in ["{","[","("]:
                stack.push(e)
            elif e in ["}","]",")"]:
                if self._match(stack.peek(),e):
                    stack.pop()
        return stack.isEmpty()
    
class PrefixToPostfix:
    def __init__(self,exp):
        self.exp = exp

    def print(self):
        print(self.exp)
    
    def convert(self):
        exp = self.exp
        revExp = exp[::-1]
        stack = Stack()
    
        for e in revExp:
            if e.isalnum():
                stack.push(e)
            else:
                a = stack.pop()
                b = stack.pop()
                temp = a + b + e
                stack.push(temp)

        return stack.toString()

e = PrefixToPostfix("*+AB-CD")
print(e.convert())


# exp = "*+AB-CD"
#exp = "-cd+ab*zb"
#print(exp)

#def prefixToPostfix(exp):
#    revExp = exp[::-1]
#    stack = Stack()
#    
#    for e in revExp:
#        if e.isalnum():
#            stack.push(e)
#        else:
#            a = stack.pop()
#            b = stack.pop()
#            temp = a + b + e
#            stack.push(temp)

#    print(stack.toString())

#prefixToPostfix(exp)
