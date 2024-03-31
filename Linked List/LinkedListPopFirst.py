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

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp_node = self.head
            self.head = temp_node.next
            if self.length == 1:
                self.tail = None  # Handle case where last node is popped
            self.length -= 1
            return temp_node.value

    def print_pop_first(self):
        popped_value = self.pop_first()
        if popped_value is not None:
            print(f"Popped value: {popped_value}")  # Print only if a value was popped

    def print_list(self):
        current_node = self.head
        print("Head:", end=" ")
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Create a linked list
linkedlist = LinkedList(1)
linkedlist.append(10)
linkedlist.append(11)
linkedlist.append(6)
linkedlist.append(100)
linkedlist.append(10)

# Print the initial list
linkedlist.print_list()

# Pop and print the first element
linkedlist.print_pop_first()

# Print the list after popping
linkedlist.print_list()
