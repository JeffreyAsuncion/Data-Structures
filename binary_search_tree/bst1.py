# Brian Faure - Python Data Structures #5 : Binary Search Tree (BST)
## Note - Omitting Delete function for now


import random


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child=None
        self.right_child=None


# BST class will be the wrapper that encases the node classes
class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        # case 1 - empty tree : insert at root
        if self.root==None:
            self.root=node(value)
        else:
            # use recursive function to traverse tree
            self._insert(value, self.root) # this will be a recursive function
    
    # private function with prefix '_'
    def _insert(self, value, cur_node):
        
        # check if value is less that current node
        if value < cur_node.value:
            # no left child
            if cur_node.left_child==None:
                # set new value as left child
                cur_node.left_child = node(value)
            # otherwise
            else:
                # traverse the tree down the left side
                self._insert(value, cur_node.left_child)
        
        # check if the value is greater
        elif value > cur_node.value:
            # check if there is a right child
            if cur_node.right_child==None:
                # set the empty right child to the new node value
                cur_node.right_child = node(value) 
            # otherwise
            else:
                # traverse the tree down the right side
                self._insert(value, cur_node.right_child)
        # if the cur node equal the value
        else: 
            print("Value already in tree!")

    def print_tree(self):
        # check if empty tree
        if self.root != None:
            # use recursive function to traverse tree
            self._print_tree(self.root)
    
    # private recusive function
    def _print_tree(self, cur_node):
        # check if empty tree
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


    def height(self):
        if self.root != None:
            # use recursive function to traverse tree
            return self._height(self.root, 0)
        else:
            return 0

    # private recursive function 
    def _height(self, cur_node, cur_height):

        if cur_node == None:
            return cur_height
        # continue down tree to and increment at each level
        left_height=self._height(cur_node.left_child, cur_height+1)
        right_height=self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, value):
        # check if root
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, cur_node):
        # case we found it
        if value == cur_node.value:
            return True
        # case value is less than cur node and left child is present
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        # case value is greater that cur node and right child is present
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        # otherwise
        else:
            return False




def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree
    

#################
# to test print tree and up

tree = binary_search_tree()
tree = fill_tree(tree)

tree.print_tree()

print("Tree height : " + str(tree.height()))

#################
# to test search
print("Tree A")
print("A" * 30)
treeA = binary_search_tree()

treeA.insert(5)
treeA.insert(1)
treeA.insert(3)
treeA.insert(2)
treeA.insert(7)
treeA.insert(10)
treeA.insert(0)
treeA.insert(20)


treeA.print_tree()

print("TreeA height : " + str(treeA.height()))

print(treeA.search(10))
print(treeA.search(30))





