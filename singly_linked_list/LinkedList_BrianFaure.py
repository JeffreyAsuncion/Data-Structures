
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur_node = self.head # starting at head of linked list
        # traverse thru the list
        while cur_node.next != None:
            cur_node = cur_node.next  # this is incrementing the node
            # traverse thru the list
        # when end of list
        cur_node.next = new_node
    
    def length(self):
        cur_node = self.head # starting at head of linked list
        total = 0
        # traverse thru the list
        while cur_node.next != None:
            total += 1
            cur_node = cur_node.next # this is incrementing the node
            # traverse thru the list
        return total
    
    def display(self):
        elems = []
        cur_node = self.head  # starting at head of linked list
        # traverse thru the list
        while cur_node.next != None:
            cur_node = cur_node.next # this is incrementing the node
            elems.append(cur_node.data)
            # traverse thru the list
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head # starting at head of linked list
        # traverse thru the list
        while True:
            cur_node = cur_node.next # this is incrementing the node
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
            # traverse thru the list
    
    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node # this keeps the place of the current 
            cur_node = cur_node.next # this iterates to next node
            if cur_idx == index:
                # erase cur_node
                last_node.next = cur_node.next # reseting pointer to erase cur_node
                return
            cur_idx += 1





my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()
print(f"the value at index(2) is {my_list.get(2)}")
my_list.erase(0)
my_list.display()