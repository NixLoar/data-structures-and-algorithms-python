class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_node(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if current is None:
            return(f"{prev_data} not found.")
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return(f"{key} not found.")

        prev.next = current.next
        current = None

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty List"


# Example on how to use it

linked_list = LinkedList()

linked_list.insert_at_beginning(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_after_node(20, 25)

print("Linked List after insertions:")
print(linked_list) 

print("\nTraversed List:")
print(linked_list.traverse())  

linked_list.delete_node(25)
print("\nLinked List after deletion:")
print(linked_list) 