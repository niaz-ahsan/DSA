from singly_ll import Linked_list

# O(n) Time | O(1) Space
def find_mid_node(ll):
    head, tail = ll.get_head_tail()
    if not head:
        return 'List doesn\'t exist'
    slow = head
    fast = head
    while fast:
        try:
            fast = fast.next.next
            if fast:
                slow = slow.next
        except:
            break
    return slow        


if __name__ == "__main__":
    ll = Linked_list()
    ll.push_all([10, 12, 8, 90, 95])
    print(ll)
    print(find_mid_node(ll))
