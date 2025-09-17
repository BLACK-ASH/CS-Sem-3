# Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert at the beginning
    def insert_from_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Insert at the end
    def insert_from_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Insert at a specific position (middle)
    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_from_head(data)
        elif position >= self.size:
            self.insert_from_tail(data)
        else:
            new_node = Node(data)
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
            self.size += 1

    # Delete from beginning
    def delete_from_head(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    # Delete from end
    def delete_from_tail(self):
        if not self.tail:
            print("List is empty.")
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1

    # Delete from a specific position (middle)
    def delete_at_position(self, position):
        if self.size == 0:
            print("List is empty.")
            return
        if position <= 0:
            self.delete_from_head()
        elif position >= self.size - 1:
            self.delete_from_tail()
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.size -= 1

    # Print list from head to tail
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    # Print list from tail to head
    def print_list_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data, end=" ")
            cur = cur.prev
        print()

    # Traverse the list (same as print_list)
    def traverse(self):
        self.print_list()


# Main function for testing with new examples
def main():
    dll = DoublyLinkedList()
    
    # Insert at head
    dll.insert_from_head(100)
    dll.insert_from_head(200)
    
    # Insert at tail
    dll.insert_from_tail(300)
    dll.insert_from_tail(400)
    
    print("List after head & tail insertions:")
    dll.print_list()
    
    # Insert at middle (position 2)
    dll.insert_at_position(250, 2)
    print("List after inserting 250 at position 2:")
    dll.print_list()
    
    # Delete from middle (position 2)
    dll.delete_at_position(2)
    print("List after deleting from position 2:")
    dll.print_list()
    
    # Delete from head
    dll.delete_from_head()
    print("List after deleting from head:")
    dll.print_list()
    
    # Delete from tail
    dll.delete_from_tail()
    print("List after deleting from tail:")
    dll.print_list()
    
    # Reverse print
    print("Reverse list:")
    dll.print_list_reverse()


# Run the main function
if __name__ == "__main__":
    main()
