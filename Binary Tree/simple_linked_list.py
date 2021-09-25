# This is for implementing a simple Queue DS
# Constant time Queue like push/pop

class Node(object):
    def __init__(self, node):
        self.node = node
        self.next = None

    def __repr__(self):
        return f'<{self.node}>' 

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # O(1) Time & Space
    def push(self, input_node):
        node = Node(input_node)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node
        self.tail = node
        self.length += 1   

    # O(1) Time & Space
    def pop(self):
        output = None
        if self.head:
            output = self.head
            self.head = self.head.next  
            self.length -= 1
        return output       

    # O(n) Time & Space
    def __repr__(self):
        if not self.head:
            return 'No list to display!'
        output = []
        curr = self.head
        while curr is not None:
            output.append(str(curr.node))
            output.append('-->')
            curr = curr.next
        return " ".join(output)      

    # O(n) Time | O(1) Space       
    def __len__(self):        
        return self.length          
                