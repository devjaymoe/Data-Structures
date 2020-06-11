"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root
            # we can check this by checking if self is None
        if self is None:
            # if not then create the node and park it there
            self = BSTNode(value)
        # otherwise, there is a root
        else:
            # compare the value to the root's value to determine which direction
            # we're gonna go in
            # if the value < root's value
            if value < self.value:
                # go left
                # how do we go left
                # we have to check if there is another node on the left
                # self.left = BSTNode(value) <-- this overwrites the left/bad
                if self.left:
                    # then self.left is a node
                    # now what?
                    self.left.insert(value)
                else:
                    # then we can park the value here
                    self.left = BSTNode(value)

            # else the value >= root's value
            else:
                # go right
                # how do we go right?
                if self.right:
                    # then self.right is a node
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return self.value
        elif target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    def iter_depth_first_for_each(self, fn):
        # with depth-first traversal, there's a certain to when we visit ondes
        # init a stack to keep track of the order of nodes we visited
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and the self second
            # to ensure that the left is popped off first
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            # call the fn function on self.value
            fn(self.value)

    def iter_breadth_first_search(self, fn):
        # uses a queue instead
        # first traversal follows FIFO ordering of its nodes
        # init a deque
        q = deque()
        # add the first node to our queue
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # print('node', node.value, 'self', self.value)
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # stack = []
        # stack.append(self)
        # while len(stack) > 0:
        #     current_node = stack.pop()
        #     if current_node.left:
        #         stack.append(current_node.left)
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
