from singly_ll import Linked_list

def find_next_eligible_node(node, seen):
    val_to_remove = node.val
    curr = node.next
    if curr:
        while curr.val == val_to_remove or curr.val in seen:
            curr = curr.next
    return curr   

# O(n) Time | O(1) Space
def remove_duplicates(ll):
    seen = {}
    head, tail = ll.get_head_tail()
    curr = head
    prev = None
    while curr:
        if curr.val in seen:
            curr =  find_next_eligible_node(curr, seen)
            prev.next = curr           
        prev = curr    
        if curr:
            seen[curr.val] = True
            curr = curr.next
        else:
            break           

if __name__ == "__main__":
    ll = Linked_list()
    #ll.push_all([12, 13, 17, 12, 17, 20, 21, 20])
    ll.push_all([12,13,13,14,14,13,13,21,14])
    remove_duplicates(ll)
    print(ll)