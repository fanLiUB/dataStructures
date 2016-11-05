# hash table

class Hash_table:
    def __init__(self,m):
        self.table = [[None]]*m
        self.size = m

    def h(self,k):
        slot = k % self.size
        return slot

    def insert(self,k):
        index = self.h(k)
        if self.table[index] == [None]:
            self.table[index] = [k]
        else:
            self.table[index].append(k)
            
    def delete(self,k):
        index = self.h(k)
        self.table[index].remove(k)

    def search(self,k):
        index = self.h(k)
        for i in range(len(self.table[index])):
            if self.table[index][i] == k:
                return k
        return ("Item not found...")

    def __str__(self):
        return (str(self.table))

    def __repr__(self):
        return (str(self.table))
