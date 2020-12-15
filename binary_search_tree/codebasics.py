class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # check if value already exist, no dups allowed in BST
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree

            # if left node already has a value
            if self.left:
                # traverse the tree
                self.left.add_child(data)
                
            # otherwise left node is empty
            else:
                # set left node with child data
                self.left = BinarySearchTreeNode(data)

        else:
            # add data in left subtree
            # if left node already has a value
            if self.right:
                # traverse the tree
                self.right.add_child(data)
                
            # otherwise right node is empty
            else:
                # set right node with child data
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        # in_order_traversal starts at the left subtree and across

        # create a holder for the results
        elements = []

        # case 1: visit left tree
        if self.left:
            # build the list of nodes
            elements += self.left.in_order_traversal()

        # case 2: visit base node
        elements.append(self.data)

        # case 3: visit right tree  
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                # there is a left tree
                return self.left.search(val)
            # left is empty
            else:
                # at a leaf node
                return False

        if val  > self.data:
            # val migh be in right subtree
            if self.right:
                # there is a right tree
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root



if __name__ == '__main__':
    countries = ["India", "Paskistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))

    print("Swenden is in the list? ", country_tree.search("Sweden"))

    print(country_tree.in_order_traversal())

# if __name__ == '__main__':

#     numbers = [17, 4, 1, 20, 9, 23, 18, 34]

#     numbers_tree = build_tree(numbers)

#     print(numbers_tree.in_order_traversal())

#     print(numbers_tree.search(20))