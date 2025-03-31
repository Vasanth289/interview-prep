from util.constants import Constants

class SinglyLinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(f"| {temp.key} |", end=" --> ")
            temp = temp.next
        print("None")

    """
    Insert a key into Singly Linked List. This method inserts the node at the end of the list
    Time Complexity: O(n)
    """
    def insert_back(self, key):
        if self.head == None:
            self.head = SinglyLinkedListNode(key)
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = SinglyLinkedListNode(key)
    
    """
    Insert a key into Singly Linked List. This method inserts the node at the beginning of the list
    Time Complexity: O(1)
    """
    def insert_front(self, key):
        if self.head == None:
            self.head = SinglyLinkedListNode(key)
            return
        
        new_node = SinglyLinkedListNode(key)
        new_node.next = self.head
        self.head = new_node

    """
    Insert a key into Singly Linked List. This method inserts a node at a specified position in the linked list
    Time Complexity: O(n)
    """
    def insert_pos(self, key, position):
        if self.head == None:
            self.head = SinglyLinkedListNode(key)
            return
        
        if position == 0:
            new_node = SinglyLinkedListNode(key)
            new_node.next = self.head
            self.head = new_node
            return
        elif position < 0:
            raise ValueError("position argument cannot be negative")

        idx = 0
        temp = self.head
        while temp.next != None and idx != position-1:
            temp = temp.next
            idx += 1
        other = temp.next
        temp.next = SinglyLinkedListNode(key)
        temp.next.next = other

    """
    Delete a key from Singly Linked List. This method deletes/removes a node from the end of the linked list
    Time Complexity: O(n)
    """
    def delete_back(self):
        if self.head == None:
            raise Exception(Constants.DELETE_EMPTY_LINKED_LIST)
        elif self.head.next == None:
            self.head = None

        curr = self.head
        prev = None
        while curr.next != None:
            prev = curr
            curr = curr.next
        prev.next = None

    """
    Delete a key from Singly Linked List. This method deletes/removes a node from the beginning of the linked list
    Time Complexity: O(1)
    """
    def delete_front(self):
        if self.head == None:
            raise Exception(Constants.DELETE_EMPTY_LINKED_LIST)
        
        temp = self.head
        self.head = self.head.next
        temp.next = None

    """
    Delete a key from Singly Linked List. This method deletes/removes a node at given position in the linked list
    Time Complexity: O(n)
    """
    def delete_pos(self, pos):
        if self.head == None:
            raise Exception(Constants.DELETE_EMPTY_LINKED_LIST)
        
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return
        
        idx = 0
        curr = self.head
        prev = None
        while curr.next != None and idx != pos:
            prev = curr
            curr = curr.next
            idx += 1
        prev.next = curr.next
        curr.next = None

class DoublyLinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        curr = self.head
        while curr != None:
            print(f"| {curr.key} |", end=" <==> ")
            curr = curr.next
        print("None")

    def insert_back(self, key):
        if self.head == None:
            self.head = DoublyLinkedListNode(key)
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        new_node = DoublyLinkedListNode(key)
        curr.next = new_node
        new_node.prev = curr