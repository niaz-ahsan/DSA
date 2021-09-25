from tree import Binary_tree
from simple_linked_list import Linked_list

# Using custom Linked list as Queue
def BFS_traversal(root):
    q = Linked_list()
    q.push(root)
    output = []
    while len(q):
        curr_node = q.pop()
        output.append(curr_node.node.val)
        if curr_node.node.left:
            q.push(curr_node.node.left)
        if curr_node.node.right:
            q.push(curr_node.node.right)
    return output         
        

if __name__ == "__main__":
    #data = [5,1,4,None,None,3,6]
    #data = [1,None,2,3]
    #data = [5,4,7,3,None,2,None,-1,None,9]
    data = [1,2,3,None,None,4,None,None,5]
    my_tree = Binary_tree()
    my_tree.construct(data)
    my_tree.display()
    print("BFS Traversal: ", end=" ")
    print(BFS_traversal(my_tree.root))

    