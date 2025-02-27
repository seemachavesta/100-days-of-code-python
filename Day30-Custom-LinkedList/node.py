class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return f'{self.data}, {self.next}'