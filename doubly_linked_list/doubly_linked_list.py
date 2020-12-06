"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        s = ""
        cur_node = self.head
        while cur_node:
            s += f"{cur_node.value} -> "
            cur_node = cur_node.next
        
        s += "None"
        return s
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create a new node
        # if empty list:
        if self.head is None:
            # set self.head = new_node
            self.head = new_node
            # set self.tail = new_node
            self.tail = new_node
        # else:
        else:
            # set self.head.prev = new_node
            self.head.prev = new_node
            # set new_node.next to self.head
            new_node.next = self.head
            # set self.head = new_node
            self.head = new_node
            # new_node.previous = None
            new_node.prev = None        
        # increment
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Check for empty pointers
        # Get previous node = node.prev
        previous_node = node.prev
        # Set prev_node.next to node.next
        if previous_node is None:
            pass
        else:
            previous_node = node.next
        # Next_node = node.next
        next_node = node.next
        # Set next_node.previous = previous_node
        if next_node is None:
            # could just call self.remove_from_head() # but dont have it right now
            pass
        else:
            next_node.prev = previous_node
        # Decrement length
        self.length -= 1
        # set node.prev = None
        node.prev = None
        # set node.next = None
        node.next = None
        # Return node.value
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if length == 0 return None
        if self.length == 0:
            return None
        # if length == 1 return self.head.value
        #################################3 check video for notes
        pass