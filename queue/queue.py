"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_from_head(self):
        if self.head is None:
            return None
        data = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return data

# Queue with Linked List
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        self.size = 0
        tracker = self.storage.head
        while tracker:
            self.size += 1
            tracker = tracker.get_next()
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        # No links
        if not self.storage.head:
            return None
        # One link
        if self.storage.head is self.storage.tail:
            one_link = self.storage.head.get_data()
            self.storage.head = None
            self.storage.tail = None
            return one_link
        # Many Links
        old_head = self.storage.head
        self.storage.head = self.storage.head.next
        return old_head.get_data()

# queue with array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         self.size = 0
#         for e in self.storage:
#             self.size += 1
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if not bool(self.storage):
#             return None
#         data = self.storage[0]
#         self.storage.pop(0)
#         return data
