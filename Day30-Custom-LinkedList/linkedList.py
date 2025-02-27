from node import Node
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    
    # Insert a value at the beginning of the linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
     # Insert a value at the end of the linked list   
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data)
        
        
     
    # Insert a value at a specific index in the linked list
    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
            
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        #Create itrator    
        itr = self.head
        count = 0
        
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                return
            
            itr = itr.next
            count += 1
            
    # Retrieve the value at a specific index      
    def get_at(self, index):
        
        if self.head == None:
            print('LinkedList is empty')
            return
      
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
            
        itr = self.head
            
        if index == 0:
            return itr.data
            
        count = 0
        while itr:
            if count == index -1:
                return itr.next.data
                
            itr = itr.next
            count += 1
            
    # Remove the value at a given index    
    def remove_at(self, index):
        if self.head == None:
            print('LinkedList is empty')
            return 
        
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                return
            
            itr = itr.next
            count += 1
            
     # Remove the first node that matches the provided value        
    def remove_by_value(self, value):
        if self.head == None:
            print('Linked List is empty')
            return
        
        if self.head.data == value:
            # Remove head if it matches
            self.head = self.head.next 
            return
            
        itr = self.head
        while itr:
            # Remove the matching node
            if itr.next.data  == value:
                itr.next = itr.next.next
                return 
            
            itr = itr.next
            
    # Return the length of the linked list
    def get_length(self):
        itr = self.head 
        count = 0
        while itr:
            itr = itr.next
            count += 1
            
        return count
        
        
    #Populate the linked list with values from a list
    def insert_values(self, list_data):
        self.head = None
        
        if not list_data:
            print('List is empty')
            return 
        
        for data in list_data:
            self.insert_at_end(data)
            
    
            
    # Search for a value in the linked list     
    def find_value(self, data):
        itr = self.head
        
        while itr:
            if itr.data == data:
                return True
          
            itr = itr.next
            
        return False
        
        
    # Print the linked list in a readable format  
    def print_list(self):
        itr = self.head
        listr = ''
        
        while itr:
            listr += str(itr.data) + ' --> '
            itr = itr.next
            
        print(listr)
        
    

    

