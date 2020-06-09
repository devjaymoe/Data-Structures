"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        elif self.tail is None:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # no head
        if not self.head:
            return None
        # if the head and tail are the same
        elif self.head == self.tail:
            oldValue = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return oldValue
        oldValue = self.head.value
        # if the head is different from the tail
        # reassign head to next on list
        self.head = self.head.next
        # clean the objects pointers
        self.head.prev = None
        self.length -= 1
        return oldValue

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # head and tail are both None
        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
            return self.tail
        # there is a tail
        elif self.tail:
            # insert new value after tail
            self.tail.insert_after(value)
            # print('next value', self.tail.next, 'current tail', self.tail)
            # print('prev pointer for new tail', self.tail.next.prev)
            self.tail = self.tail.next
            self.length += 1
        else:
            # there is no tail/make tail node and make its prev the head
            self.tail = ListNode(value, self.head)
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # head and tail are the same
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return None
        # there is a tail
        elif self.tail:
            # delete the tail
            old_tail = self.tail
            self.tail = self.tail.prev
            old_tail.delete()
            self.length -= 1
            return old_tail.value
        else:
            # no tail return none
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
