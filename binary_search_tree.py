# binary search tree

class BST:
    # constructs a binary-search-tree with size n rooted at index 0
    def __init__(self,n):
        self.tree = [None] * n
        self.size = n

    def root(self):
        return self.tree[0]

    def parent(self,i):
        if i == 0:
            return 0
        else:
            return (i-1)//2

    def left(self,i):
        return i*2 + 1

    def right(self,i):
        return i*2 + 2

    # inserts k to the BST rooted at r
    def insert(self,r,k):
        if self.tree[r] == None:
            self.tree[r] = k
        elif self.tree[r] >= k:
            self.insert(self.left(r),k)
        else:
            self.insert(self.right(r),k)

    # deletes k from the BST rooted at r
    def delete(self,r,k):
        if self.tree[k] == None:
            return ("None")
        elif self.left(k) < self.size and self.tree[self.left(k)] == None:
            self.transplant(k,self.right(k))
        elif self.right(k) < self.size and self.tree[self.right(k)] == None:
            self.transplant(k,self.left(k))
        else:
            y = self.minimum(self.right(k))[0]
            if self.parent(y) != k:
                self.transplant(y,self.parent(y))
                self.tree[self.right(y)] = self.tree[self.right(k)]
                self.tree[self.parent(self.right(y))] = self.tree[y]
            self.transplant(k,y)
            self.tree[self.left(y)] = self.tree[self.left(k)]
            self.tree[self.left(self.parent(y))] = self.tree[y]

    # replaces the subtree rooted at u with the subtree rooted at v
    # does not affect v's children
    def transplant(self,u,v):
        if u == 0:
            self.tree[0] = self.tree[v]
        elif u == self.left(self.parent(u)):
            self.tree[self.left(self.parent(u))] = self.tree[v]
        else:
            self.tree[self.right(self.parent(u))] = self.tree[v]
        if self.tree[v] != None:
            self.tree[self.parent(v)] = self.tree[self.parent(u)]


    # returns (index_of_k, k) if k is in BST rooted at r
    def search(self,r,k):
        if self.tree[r] == k:
            return (r,k)
        elif self.tree[r] == None:
            return ("None")
        elif self.tree[r] >= k:
            return self.search(self.left(r),k)
        else:
            return self.search(self.right(r),k)

    # returns the index of min key and its value in BST rooted at r
    def minimum(self,r):
        m = self.tree[r]
        while r < self.size and self.tree[r] != None:
            m = self.tree[r]
            r = self.left(r)
        return (self.parent(r),m)

    # returns the index of max key and its value in BST rooted at r
    def maximum(self,r):
        m = self.tree[r]
        while r < self.size and self.tree[r] != None:
            m = self.tree[r]
            r = self.right(r)
        return (self.parent(r),m)
    
    def __str__(self):
        return (str(self.tree))

    def __repr__(self):
        return (str(self.tree))
