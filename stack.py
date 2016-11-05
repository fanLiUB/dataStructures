# stack

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)
    
    def top(self):
        if self.isEmpty() == True:
            return ("Error: the stack is empty")
        return self.items[self.size()-1]

    def pop(self):
        if self.isEmpty() == True:
            return ("Error: the stack is empty")
        r = self.items.pop()
        return r

    def __str__(self):
        return (str(self.items))

    def __repr__(self):
        return (str(self.items))
