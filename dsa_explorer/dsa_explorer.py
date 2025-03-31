import argparse
from datastructures.linked_list import SinglyLinkedList, DoublyLinkedList

def main():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert_back(1)
    singly_linked_list.insert_back(2)
    singly_linked_list.insert_back(3)
    singly_linked_list.insert_back(4)
    singly_linked_list.insert_back(5)
    singly_linked_list.print_linked_list()
    singly_linked_list.delete_back()
    singly_linked_list.print_linked_list()
    print()

    other_singly_linked_list = SinglyLinkedList()
    other_singly_linked_list.insert_front(1)
    other_singly_linked_list.insert_front(2)
    other_singly_linked_list.insert_front(3)
    other_singly_linked_list.insert_front(4)
    other_singly_linked_list.insert_front(5)
    other_singly_linked_list.print_linked_list()
    other_singly_linked_list.delete_front()
    other_singly_linked_list.print_linked_list()
    print()

    another_singly_linked_list = SinglyLinkedList()
    another_singly_linked_list.insert_pos(1, 0)
    another_singly_linked_list.insert_pos(2, 0)
    another_singly_linked_list.insert_pos(3, 2)
    another_singly_linked_list.insert_pos(4, 1)
    another_singly_linked_list.insert_pos(5, 2)
    another_singly_linked_list.print_linked_list()
    another_singly_linked_list.delete_pos(2)
    another_singly_linked_list.print_linked_list()
    print()

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_back(1)
    doubly_linked_list.insert_back(2)
    doubly_linked_list.insert_back(3)
    doubly_linked_list.insert_back(4)
    doubly_linked_list.insert_back(5)
    doubly_linked_list.print_linked_list()

if __name__ == "__main__":
    main()