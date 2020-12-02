
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head # start at head of list
        while cur.next != None:
            cur = cur.next # this is to transverse the list
        # now at the end of the list add new node
        cur.next = new_node   

    def length(self):
        cur = self.head # initialize a starting point
        total = 0 # num of nodes so far
        while cur.next != None: # transverse the linked list
            total += 1 # count the nodes as we pass by
            cur = cur.next # transverse the linked list
        # now at the end of list 
        return total

    def display(self):
        elems = [] # initalize a list to store the values of linked list
        cur_node = self.head # initialze a starting point
        while cur_node.next != None:
            cur_node = cur_node.next # transverse the linked list
            elems.append(cur_node.data)
        print(elems)

    def get(self, index): # extract data from linked list
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0 # variable to track the current index
        cur_node=self.head
        while True:
            cur_node=cur_node.next # transverse or increment the node
            if cur_idx == index:
                print("Found it!")
                return cur_node.data
            #otherwise increment and move to next 
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
        cur_idx = 0 # variable to track index count or current index
        cur_node=self.head # initialize starting point in linked list
        while True:
            # when erasing a node, we need a place holder
            last_node = cur_node
            cur_node = cur_node.next # increment to next node
            if cur_idx == index:
                # we don't have to delete the node
                # we just have to point to the node.next of the cur_node @ index
                last_node.next = cur_node.next
                return
            # didn't find it yet keep going
            cur_idx += 1



my_list = linked_list() 

my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()
index = 2
print("element at {}th index is {}".format(index, my_list.get(index)))
print("length is {}".format(my_list.length()))

index = 1
my_list.erase(index)
print("now erase at index {}".format(index))
my_list.display()








