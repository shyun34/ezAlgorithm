class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return 1

        return 0

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.empty():
            return -1

        ret_data = self.head.data

        self.head = self.head.next

        return ret_data

    def peek(self):
        if self.empty():
            return -1

        return self.head.data