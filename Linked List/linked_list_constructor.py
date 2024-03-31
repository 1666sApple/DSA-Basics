class LinkedList:
    def __init__(self, value):
        
        # create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # def append(self, value):
        #create a new node 
        #add Node to end
    # def prepend(self, value):
        #create a new node
        #add Node to beginning 
    # def insert(self, index, value):
        #create a new node
        #add Node to index
        
# Here for the same operation as creating a new node occurs, we create a separate class named node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def print_list(self):
    current_node = self.head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

# Here we create a new linked list
linked_list = LinkedList(4)
print_list(linked_list)