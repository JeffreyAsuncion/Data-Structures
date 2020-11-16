"""
Linked Lists are composed of Node
NOT inheritance of Node

video CS02_Data_Structures_1
"""

"""
Elissa Thomas
"""

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):    # getter
#         return self.value
    
#     def get_next_node(self):
#         return self.next_node
    
#     def set_next_node(self, new_next):
#         self.next_node = new_next


# class LinkedList:
#     def __init__(self):
#         # what attributes do we need?
#         # start with an empty list
#         self.head = None
#         self.tail = None

#     def add_to_head(self, value):
#         # create a new Node
#         new_node = Node(value)
        
#         # case 1 if LinkedList is empty
#         if self.head is None:
#             ## create a new Node    # see before if
#             # update head and tail attributes
#             self.head = new_node
#             self.tail = new_node
        
#         # case 2 LinkedList has 1 item
#         # code for case 2 is same as case 3   

#         # case 3 for existing LinkedList
#         else:
#             ## create a new Node    # see before if
#             # set next_node of my new Node to the head
#             new_node.set_next_node(self.head)
#             # update head attribute
#             self.head = new_node


#     def add_to_tail(self, value):
#         # create a new Node
#         new_node = Node(value)
#         # 1. LL is empty
#         if self.head is None:
#             # update head and tail attributes
#             self.head = new_node
#             self.tail = new_node
#         # 2. LL is not empty
#         else:
#             # update next_node of our tail
#             self.tail.set_next_node(new_node) # old tail point to new_node / new tail
#             # update self.tail
#             self.tail = new_node 
####### 1:20:30

#     def remove_head(self):
#         # case 1 - empty list
#         if self.head is None:
#             return None
#         else:
#             # case 2 - list with one item
#             ret_value = self.head.get_value() # save value before remove head
#             if self.head == self.tail:
#                 self.head = None
#                 self.tail = None
#             # case 2 - list with 2+ elements - return VALUE of old head
#             else:
#                 self.head = self.head.get_next_node()
#                 return ret_value


#     def remove_tail(self):
#         # TODO
#         pass

#     def contains(self, value):
#         # TODO time permitting
#         pass

#     def get_max(self):
#         # TODO time permitting
#         pass




"""
CPT11 - Glenna Yu
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next # point to the next node in the list

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head: Node = None # points to the first node in the list
        self.tail: Node = None # points to the last node in the list
        self.length = 0

    # append / add --> add_to_tail
    def add_to_tail(self, value): # Constant time O(1)
        #Check if there's a tail
        # if there is no tail (empty list)
        if not self.tail: # Could also check length, check if tail = None
        # Create a new node
            new_tail = Node(value, None)
        # Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
        # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
        # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
        # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1


    # remove
    def remove_head(self):
        # if not nead (empty list)
        if not self.head:   # if self.head is None
            return None
        #   Return None

        # List with one element
        if self.head == self.tail:   #self.length = 1 is also valid
        # Set self.head to current_head.next (which is also None)    
            current_head = self.head
            self.head = None
        # Set self.tail to None
            self.tail = None
            self.length -= 1
            return current_head.value        
        # Decrement length by 1
        
        # Check if head (general case):
        else:
        #   Set self.head to current_head.value
            current_head = self.head
            self.head = current_head.next
        #       Return current_head.value
            self.length -= 1
            return current_head.value



    def remove_tail(self):
        # Remove Tail:
        # Check if it's there
        # General case:
        # Start at head and iterate to the next-to-last node
        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        #
        # List of 1 element
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
        pass
