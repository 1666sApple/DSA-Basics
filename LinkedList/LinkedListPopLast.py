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

    def pop_last(self):
        if self.length == 0:
            return None

        if self.length == 1:  # Handle single-node case
            value = self.head.value
            self.head = self.tail = None
            self.length = 0
            return value

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        value = self.tail.value
        self.tail = current_node
        self.tail.next = None
        self.length -= 1
        return value

    def print_pop_last(self):
        popped_value = self.pop_last()
        if popped_value is not None:
            print(f"Popped value: {popped_value}")

    def print_list(self):
        current_node = self.head
        print("Head:", end=" -> ")
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Test the linked list
linkedlist = LinkedList(1)
linkedlist.append(10)
linkedlist.append(11)
linkedlist.append(6)
linkedlist.append(100)
linkedlist.append(10)

# Initial list
linkedlist.print_list()

# Pop and print
linkedlist.print_pop_last()

# List after popping
linkedlist.print_list()
