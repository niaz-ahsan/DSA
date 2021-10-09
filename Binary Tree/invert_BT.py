from tree import Binary_tree

# swap current node's left and right children and move to left and then right.

def inversion_helper(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    inversion_helper(node.left)
    inversion_helper(node.right)    

def invert(tree):
    inversion_helper(tree.root)

if __name__ == "__main__":
    #tree_data = [1,2,3,None,None,4,None,None,5]
    tree_data = [4,2,7,1,3,6,9]
    tree = Binary_tree()
    tree.construct(tree_data)
    tree.display()
    invert(tree)
    print("After inversion:")
    tree.display()
    