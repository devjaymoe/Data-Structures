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

    def remove_tail(self):
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node 
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head
            # traverse until we get to the Node right 
            # before the tail Node 
            while current.get_next() != self.tail:
                current = current.get_next()
            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = current
        return data

    def remove_head(self):
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

    def contains(self, value):
        if not self.head:
            return None
        # go though list
        if self.head.data == value:
            return self.head.data
        truthy_tracker = self.head.next
        while truthy_tracker:
            # check if value at node is value
            if value == truthy_tracker.data:
            # if it is stop list
                return truthy_tracker.data
            truthy_tracker = truthy_tracker.next
        # return node at value

    def get_max(self):
        if not self.head:
            return None
        max = self.head.data
        tracker = self.head
        while tracker:
            if tracker.data > max:
                max = tracker.data
            tracker = tracker.next
        return max