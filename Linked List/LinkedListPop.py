class LinkedList:
    
    def __init__(self, value):
        # create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        # create a new node 
        new_node = Node(value)
        # add Node to end
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        if self.head is None:
            return None
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            self.tail = previous_node
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return current_node.value  
        
    # def prepend(self, value):
        # create a new node
        # add Node to beginning 
    # def insert(self, index, value):
        # create a new node
        # add Node to index
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        
# Here for the same operation as creating a new node occurs, we create a separate class named node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    


# Here we create a new linked list
linked_list = LinkedList(4)
linked_list.append(5)

print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())

