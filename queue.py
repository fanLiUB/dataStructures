# queue

class Queue:
    def __init__(self,c):
        self.items = [None]*c
        self.tail = 0
        self.head = 0
        self.capacity = c
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.capacity == self.size

    def enqueue(self,x):
        self.items[self.tail] = x
        if self.size < self.capacity:
            self.size += 1
        self.tail += 1
        if self.tail == self.capacity:
            self.tail = 0
            
    def dequeue(self):
        r = self.items[self.head]
        self.items[self.head] = None
        if self.size > 0:
            self.size -= 1
        self.head += 1
        if self.head == self.capacity:
            self.head = 0
        return r

    def __str__(self):
        return (str(self.items))

    def __repr__(self):
        return (str(self.items))
