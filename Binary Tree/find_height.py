from tree import Binary_tree

if __name__ == "__main__":
    tree_data = [1,2,3,4,5,6,None,None,None,None,None,7,8]
    tree = Binary_tree()
    tree.construct(tree_data)
    tree.display()
    print("Height is: " + str(tree.height()))

