

from typing import List

# Creating a Singly Linked List
# creating node class for defining node values & references
class Node:
    def __init__(self, value = None) -> None:
        # value coming from the parameter or use by-default None
        self.value = value
        self.next = None

# creating linked list class to connect nodes 
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # printing the contents of linked list 
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next



# creating an object for class
singlyLinkedList = SinglyLinkedList()

# Creating two nodes for our linked list 
node1 = Node(1)
node2 = Node(2)

# Linking both the nodes together
singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

# printing/ visualizing our linked list 
singlyLinkedList.printLinkedList()