from tree import Binary_tree

# left -> parent -> right
def inorder_traversal(node = None, output = []):
    if node.left:
        inorder_traversal(node.left, output)
    output.append(node.val)
    if node.right:
        inorder_traversal(node.right, output) 
    return output 

# parent -> left -> right
def preorder_traversal(node = None, output = []): 
    output.append(node.val)
    if node.left:
        preorder_traversal(node.left, output)
    if node.right:
        preorder_traversal(node.right, output) 
    return output 

# left -> right -> parent
def postorder_traversal(node = None, output = []): 
    if node.left:
        postorder_traversal(node.left, output)
    if node.right:
        postorder_traversal(node.right, output) 
    output.append(node.val)    
    return output             

if __name__ == "__main__":
    tree_data = [1,2,3,None,None,4,None,None,5]
    tree = Binary_tree()
    tree.construct(tree_data)
    tree.display()
    print("Inorder traversal: ", end="")
    print(inorder_traversal(tree.root))
    print("Preorder traversal: ", end="")
    print(preorder_traversal(tree.root))
    print("Postorder traversal: ", end="")
    print(postorder_traversal(tree.root))
