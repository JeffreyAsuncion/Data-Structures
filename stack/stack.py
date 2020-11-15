"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


"""
https://www.geeksforgeeks.org/stack-data-structure-introduction-program/
"""
from sys import maxsize

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.storage = ?

    def __len__(self):
        self.size = len(self.storage)
        return self.size


    def push(self, value):
        self.storage.append(value)
        #print(value + " pushed to stack")

    def pop(self):
        # if self.size<=0:
        #     return ("Stack Empty!")
        # item = self.storage.pop()
        # self.top -= 1
        # return item
        if not self.storage:
            return str(-maxsize - 1) # return minus inifinite
        return self.storage.pop()