class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) Time & Space
    def push_at_tail(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    # O(1) Time & Space
    def push_at_head(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node  

    # O(1) Time & Space
    def delete_from_head(self):
        if self.head:
            self.head = self.head.next

    # O(n) Time | O(1) Space
    def delete_by_value(self, val):
        prev = None
        curr = self.head
        if val == self.head.val:
            self.delete_from_head()
            return True
        while curr:
            if curr.val == val:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True    
            prev = curr
            curr = curr.next
        return False            

    def get_head_tail(self):
        return (self.head, self.tail)

    def set_head_tail(self, head, tail):
        self.head = head
        self.tail = tail

    # Call this method if cyclic list is targeted
    def create_loop(self):
        if self.head.next:
            self.tail.next = self.head

    # Method to check if cyclic list is created!
    def print_cyclic_ll(self):
        if not self.head:
            return 'No list to display!'
        output = []
        max_iter = 20
        i = 0
        curr = self.head
        while curr and i <= max_iter:
            output.append(str(curr.val))
            output.append('-->')
            curr = curr.next
            i += 1
        return " ".join(output)             

    # O(n) Time & O(1) Space
    def search(self, val):
        curr = self.head
        while curr is not None:
            if curr.val == val:
                return True
            curr = curr.next    
        return False                

    # O(n) Time | O(1) Space       
    def __len__(self):
        if self.head is None:
            return 0
        len = 0
        curr = self.head
        while curr is not None:
            len += 1
            curr = curr.next
        return len        

    # O(n) Time & Space
    def __repr__(self):
        if not self.head:
            return 'No list to display!'
        output = []
        curr = self.head
        while curr is not None:
            output.append(str(curr.val))
            output.append('-->')
            curr = curr.next
        return " ".join(output)            




if __name__ == "__main__":
    ll = Linked_list()
    ll.push_at_head(5)
    ll.push_at_head(8)
    ll.push_at_tail(-1)
    ll.push_at_head(10)
    print(len(ll), ll) # using dunder __repr__ method
    # print(len(ll)) # using dunder __len__ method
    ll.delete_by_value(-1)
    print(len(ll), ll)
