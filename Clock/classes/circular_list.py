
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def create_clock(self):
        for i in range(1, 13):
            self.insert(i)
            
    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result
