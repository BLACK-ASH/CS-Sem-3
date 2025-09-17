# Node class for singly linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class to manage tasks
class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_task(self, task):
        if not self.head:  # List is empty
            return False
        if self.head.data == task:
            self.head = self.head.next  # Remove head node
            return True
        curr = self.head
        while curr.next:
            if curr.next.data == task:
                curr.next = curr.next.next  # Bypass the node
                return True
            curr = curr.next
        return False  # Task not found

    def display_tasks(self):
        if not self.head:
            print("Task list is empty")
            return
        print("Task list:")
        curr = self.head
        while curr:
            print(" -", curr.data)
            curr = curr.next

    def search_task(self, keyword):
        curr = self.head
        found = False
        keyword = keyword.lower()
        while curr:
            if keyword in curr.data.lower():
                print(f"Found: {curr.data}")
                found = True
            curr = curr.next
        if not found:
            print("No matching task found")


# Example Usage

# Create an instance of TaskList
todo = TaskList()

# Add tasks to the list
todo.add_task("Prepare monthly financial report")
todo.add_task("Email project updates to team")
todo.add_task("Schedule client meeting for next week")
todo.add_task("Organize files and documents")
todo.add_task("Update website with new content")

# Display all tasks
todo.display_tasks()

# Remove a task
print("\nRemoving 'Organize files and documents'")
todo.remove_task("Organize files and documents")

# Display updated list of tasks
todo.display_tasks()

# Search for tasks containing 'project'
print("\nSearching for 'project':")
todo.search_task("project")

# Display tasks again to confirm state
todo.display_tasks()
