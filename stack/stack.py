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

https://www.knowledgehut.com/blog/programming/how-to-implement-python-stack
"""

"""
Condition 1. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
"""

# from sys import maxsize
# 
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []


#     def __len__(self):
#         #self.size = len(self.storage)
#         return self.size

#     # Function to add an item from stack. It increases size by 1
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#         #print(value + " pushed to stack")

#     # Function to remove an item from stack. It decreases size by 1
#     def pop(self):
#         # if the storage is empty
#         if not self.storage:
#             #return None
#             return None
#         # otherwise 
#         # decrement size
#         # storage.pop
#         self.size -= 1
#         return self.storage.pop()
#
#     #Function to return the top from the stack without removing it
#     def peek(self):
#         if (isEmpty(stack)):
#             return None
#         return self.storage[self.size -1]  



"""
Condition #2

2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""

# Python program for linked list implementation of stack

# Class to represent a node
class StackNode:
    # Constructor to initalize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Constructor to initialize the root of linked list
    def __init__(self): # good
        self.root = None
        self.size = 0

    def isEmpty(self):
        empty = False
        if self.root is None:
            empty = True
        return empty

    def __len__(self): # good
        return self.size

    # Function to add an item from stack. It increases size by 1
    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.root
        self.root = new_node
        self.size += 1
    
    
    # Function to remove an item from stack. It decreases size by 1
    def pop(self):
        if (self.isEmpty()):
            return None
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        self.size -= 1
        return popped

        
    #Function to return the top from the stack without removing it
    def peek(self):
        if self.isEmpty():
            return None
        return self.root.data






