from utils.node import Node

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None

    def insert_at_beginning(self, task):
        # Insert a new task at the beginning of the list
        node = Node(task, self.head)
        self.head = node


    def print_recently_completed(self):
        # Print all recently completed tasks from the linked list
        if not self.head:
            print("There are no completed tasks to display.")

        itr = self.head
        while itr:
            print(f"Task ID: {itr.task.id} - {itr.task.title} - Due Date: {itr.task.due_date}")
            itr = itr.next



    
     