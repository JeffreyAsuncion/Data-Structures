# Brian Faure - Python Data Structures #5 : Binary Search Tree (BST)
# Including the deletion functionality

import random


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child=None
        self.right_child=None
        self.parent=None # pointer to parent node in tree


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
                # include parent
                cur_node.left_child.parent=cur_node  # set parent
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
                # include parent
                cur_node.right_child.parent=cur_node # set parent
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


    # returns the node with specified input value
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    
    # delete value :  delete value will be passed an integer and will call delete_node
    def delete_value(self, value):
        return self.delete_node(self.find(value))

    # delete node : will be passed a node
    def delete_node(self, node):

        # return the node with min value in a tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child != None:
                current=current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children
        
        # get the parent of the node to be deleted
        node_parent=node.parent

        # get the number of children of the node to be deleted
        node_children=num_children(node)

        # break operation into different cases based on the 
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children==0:

            # remove reference to the node from the parent
            if node_parent.left_child==node:
                node_parent.left_child=None
            else:
                node_parent.right_child=None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child # new variable to hold child
            else:
                child = node.right_child

            # replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child 
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent=node_parent

        # CASE 3 (node has two children)
        if node_children==2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was 
            # copied into the other node
            self.delete_node(successor)



    # returns true if the value exists in the tree
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

##################################
# case one delete the root

print("Test the delete")

print("Delete" * 5)

treeB = binary_search_tree()

treeB.insert(5)
treeB.insert(4)
treeB.insert(6)
treeB.insert(10)
treeB.insert(9)
treeB.insert(11)

treeB.print_tree()

treeB.delete_value(5)

print("del 5")

treeB.print_tree()


##############
# next case delete a child

print("del a leaf")

treeB.delete_value(4)
treeB.print_tree()

##############
# next case

print("del another leaf")

treeB.delete_value(11)
treeB.print_tree()

############3
# next case 

print("del parent with child")

treeB.delete_value(9)
treeB.print_tree()
