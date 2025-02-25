class Node:
    """A Node of a singly linked list"""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

class LinkedList:
    """Singly Linked List"""
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    def insert_at_end(self, data):
        """Insert a node at the end of the linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """Delete a node by value"""
        temp = self.head

        # If head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if not temp:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_beginning(0)
llist.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
llist.delete_node(2)
llist.display()  # Output: 0 -> 1 -> 3 -> None
