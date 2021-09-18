from singly_ll import Linked_list

def get_cycle_init_node(ll, left, right):
    while left != right:
        left = left.next
        right = right.next
    return left    

# Floyd's hare & tortoise algorithm
def is_cyclic(ll):
    cycle_exists = False
    head, tail = ll.get_head_tail()
    slow = head
    fast = head
    if not fast:
        return cycle_exists    
    while fast:
        try:
            slow = slow.next
            fast = fast.next.next
        except:
            break
        if slow == fast:
            cycle_exists = True
            break    
    if cycle_exists:
        print('loop begins at:', end=" ")
        head, tail = ll.get_head_tail()
        cycle_init_node = get_cycle_init_node(ll, head, slow)
        print(cycle_init_node.val)
    return cycle_exists        
    

if __name__ == "__main__":
    ll = Linked_list()
    ll.push_at_tail(7)
    ll.push_at_tail(14)
    ll.push_at_tail(27)
    ll.create_loop()
    #print(ll.print_cyclic_ll())
    print(is_cyclic(ll))
