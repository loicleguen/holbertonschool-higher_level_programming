#!/usr/bin/python3
"""
Module defines a node of a singly linked list
"""


class Node:
    """Class that defines a node"""

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif new_node.data < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node and
                   current.next_node.data < new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
