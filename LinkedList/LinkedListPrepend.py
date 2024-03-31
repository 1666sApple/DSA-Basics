class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def print_list(self):
        current = self.head
        print(f"Head: {current.value}", end=" -> ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        print(f"Tail: {linkedlist.tail.value}")

linkedlist = LinkedList(1)
linkedlist.append(10)
linkedlist.append(11)
linkedlist.append(6)
linkedlist.append(100)
linkedlist.append(10)
linkedlist.print_list()

linkedlist.prepend(1000)
linkedlist.print_list()
