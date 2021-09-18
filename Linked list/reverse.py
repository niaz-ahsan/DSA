from singly_ll import Linked_list

# O(n) Time | O(1) Space
def reverse(ll):
    head, tail = ll.get_head_tail()
    set_tail_later = head
    prev_node = None
    curr_node = head
    next_node = curr_node.next
    while curr_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        if next_node:
            next_node = next_node.next
    ll.set_head_tail(prev_node, set_tail_later)        
    return ll    

if __name__ == "__main__":
   ll = Linked_list()
   ll.push_at_tail(10)
   ll.push_at_tail(13)
   ll.push_at_tail(200)
   ll.push_at_tail(40)
   print(ll)
   reverse(ll)
   print(ll)
    