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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        self.size = 0
        for e in self.storage:
            self.size += 1
        return self.size

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if not bool(self.storage):
            return None
        data = self.storage[len(self.storage) - 1]
        self.storage.pop()
        return data

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        # returns the node's data
        return self.data

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference
        return self.next
    
    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next = new_next

class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    def add_to_tail(self, data):
        # adds `data` to the end of the LinkedList
        # wrap the `data` in a Node Instance
        new_node = Node(data)

        # what about the empty case, where both head and tail are None
        if not self.head and not self.tail:
            # list is empty
            # update both head and tail to point to the new node
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node

    def remove_from_head(self):
        # removes the Node that `self.head` is referering to and returns the
        # Node's data
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_data()

        # both head and tail refer to the same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list
            # delete the head Node
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data