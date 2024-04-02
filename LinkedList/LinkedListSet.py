class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.Head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        
    def set_value(self, index, value):
        try:
            if index < 0 or index >= self.length:
                raise IndexError("Index out of range")
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value
            return current_node.value
        except IndexError as e:
            print(f"Error: {e}") 
            return None 

        
    def print_list(self):
        current_node = self.Head
        while current_node is not None:
            print(f"{current_node.value}", end=" -> ")
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

print(linkedlist.set_value(13, 10))
